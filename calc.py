while True:
    a = int(input())
    b = int(input())
    symbol = input()

    if symbol == "+":
        print(str(a) + " + " + str(b) + " = " + str(a+b))
        pass
    elif symbol == "-":
        print(str(a) + " - " + str(b) + " = " + str(a - b))
        pass
    elif symbol == "*":
        print(str(a) + " * " + str(b) + " = " + str(a * b))
        pass
    elif symbol == "/":
        print(str(a) + " / " + str(b) + " = " + str(a / b))
        pass
    else:
        print("Неверно введена операция, повторите")


