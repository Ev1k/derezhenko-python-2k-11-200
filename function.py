def find_max(*args):
    max_value = -1000
    for i in range(len(args)):
        if (max_value < int(args[i])):
            max_value = int(args[i])
    print(max_value)

find_max(1, 2, 3, 6, 10, 0, 1000)
