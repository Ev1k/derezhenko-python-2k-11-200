def valueError_handler_decorator(func):
    def wrapper(*args, **kwargs):
        print("Ввод: ", *args, **kwargs)
        item0 = args[0]
        for item in args:
            if (type(item) != type(item0)):
                return None
        print("Вывод: ", func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrapper
