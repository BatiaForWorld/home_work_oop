class MixinLog:
    """
    Миксин для логирования создания объектов.

    При создании объекта выводит информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализирует объект с логированием.

        """

        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())

        all_params = []
        if args_str:
            all_params.append(args_str)
        if kwargs_str:
            all_params.append(kwargs_str)

        params = ", ".join(all_params)

        print(f"{self.__class__.__name__}({params})")

        super().__init__(*args, **kwargs)
