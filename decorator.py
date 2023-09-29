from wrapper import valueError_handler_decorator


@valueError_handler_decorator
def find_max(*args):
    max_value = -1000
    for item in args:
        if (max_value < item):
            max_value = item
    return max_value


print(find_max(1, 2, 3, 10, 0, 1000, "fgf"))
