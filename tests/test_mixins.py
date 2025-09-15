from src.mixins import MixinLog


class SimpleMixin(MixinLog):
    """Тестовый класс, наследующий от MixinLog для тестирования миксина."""

    def __init__(self, value):
        self.value = value

        super().__init__()


class SuperMixin(MixinLog):
    """Тестовый класс для проверки работы super() в миксине."""

    def __init__(self, name):
        self.name = name

        super().__init__()


def test_mixin_log_basic_functionality():
    """Проверка базовой функциональности MixinLog."""

    test_obj = SimpleMixin("test_value")

    assert test_obj.value == "test_value"


def test_mixin_log_super_call_fallback():
    """Тест для проверки fallback логики в MixinLog."""

    obj = SuperMixin("test")
    assert obj.name == "test"


def test_mixin_log_output_formatting(capsys):
    """Проверка форматирования вывода миксина."""

    from src.base_product import BaseProduct

    class TestMixinWithParams(MixinLog, BaseProduct):
        def __init__(self, name, description, extra_param=None):
            self.extra_param = extra_param
            super().__init__(name, description)

        def __str__(self):
            return f"TestMixinWithParams: {self.name}"

        def __repr__(self):
            return f"TestMixinWithParams('{self.name}')"

    obj = TestMixinWithParams("test_name", "test_desc", extra_param="extra")

    assert obj.name == "test_name"
    assert obj.description == "test_desc"

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "TestMixinWithParams(" in output
    assert "'test_name'" in output
    assert "'test_desc'" in output


def test_mixin_log_with_no_args(capsys):
    """Проверка работы миксина без аргументов."""

    class TestMixinNoArgs(MixinLog):
        def __init__(self):
            super().__init__()

    obj = TestMixinNoArgs()

    assert isinstance(obj, TestMixinNoArgs)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "TestMixinNoArgs()" in output


def test_mixin_log_with_only_kwargs(capsys):
    """Проверка работы миксина с keyword аргументами в BaseProduct."""
    from src.base_product import BaseProduct

    class TestMixinKwargs(MixinLog, BaseProduct):
        def __init__(self, name="default", description="default_desc"):
            super().__init__(name, description)

        def __str__(self):
            return f"TestMixinKwargs: {self.name}"

        def __repr__(self):
            return f"TestMixinKwargs('{self.name}')"

    obj = TestMixinKwargs(name="test_name", description="test_desc")

    assert obj.name == "test_name"
    assert obj.description == "test_desc"

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "TestMixinKwargs(" in output
    assert "test_name" in output
    assert "test_desc" in output


def test_mixin_log_with_only_args(capsys):
    """Проверка работы миксина с позиционными аргументами."""
    from src.base_product import BaseProduct

    class TestMixinArgs(MixinLog, BaseProduct):
        def __init__(self, name, description):
            super().__init__(name, description)

        def __str__(self):
            return f"TestMixinArgs: {self.name}"

        def __repr__(self):
            return f"TestMixinArgs('{self.name}')"

    obj = TestMixinArgs("arg1", "arg2")

    assert obj.name == "arg1"
    assert obj.description == "arg2"

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "TestMixinArgs(" in output
    assert "'arg1'" in output
    assert "'arg2'" in output


def test_mixin_log_inheritance():
    """Проверка что MixinLog можно использовать в наследовании."""

    assert isinstance(MixinLog, type)

    assert issubclass(SimpleMixin, MixinLog)
    assert issubclass(SuperMixin, MixinLog)


def test_mixin_log_method_resolution_order():
    """Проверка что MixinLog корректно участвует в MRO."""

    class BaseClass:
        def __init__(self, value):
            self.base_value = value

    class TestMultipleMixin(MixinLog, BaseClass):
        def __init__(self, value):
            super().__init__(value)

    mro = TestMultipleMixin.__mro__
    assert TestMultipleMixin in mro
    assert MixinLog in mro
    assert BaseClass in mro

    obj = TestMultipleMixin("test_value")
    assert obj.base_value == "test_value"
