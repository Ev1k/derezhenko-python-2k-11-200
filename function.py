def find_max(*args):
    max_value = -1000
    for item in args:
        if (max_value < int(item)):
            max_value = int(item)
    print(max_value)

find_max(1, 2, 3, 6, 10, 0, 1000)
