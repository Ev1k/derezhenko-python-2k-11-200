def valueError_handler_decorator(func):
    def wrapper(*args, **kwargs):
        print("Ввод: ", *args, **kwargs)
        for i in range(len(args)):
            if (type(args[i]) != str) and (type(args[i]) != bool):
                continue
            else:
                return None
        return print("Вывод: ", func(*args, **kwargs))
    return wrapper
