lst = input().split()


def use_list_comprehensions(lst):
    lst = [int(x) for x in lst]
    lst_odd_num = [x for x in lst if x % 2 == 1]
    lst_even_num = [x for x in lst if x % 2 == 0]
    lst_less_than0 = [x for x in lst if x < 0]
    print_result(lst_odd_num, lst_even_num, lst_less_than0)


def use_functions(lst):
    lst = list(map(lambda x: int(x), lst))
    lst_even_num = list(filter(lambda x: x % 2 == 0, lst))
    lst_odd_num = list(filter(lambda x: x % 2 == 1, lst))
    lst_less_than0 = list(filter(lambda x: x < 0, lst))
    print_result(lst_odd_num, lst_even_num, lst_less_than0)


def print_result(lst_odd_num, lst_even_num, lst_less_than0):
    print("Нечетные: ", lst_odd_num)
    print("Чётные: ", lst_even_num)
    print("Меньше 0: ", lst_less_than0)


try:
    use_list_comprehensions(lst)
    use_functions(lst)
except ValueError:
    print(-1)
