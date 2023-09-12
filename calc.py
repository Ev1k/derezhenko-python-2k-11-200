plus_operations = []
minus_operations = []
con_operations = []
div_operations = []

while True:
    a = int(input())
    b = int(input())
    symbol = input()

    if symbol == "+":
        res = str(a) + " + " + str(b) + " = " + str(a+b)
        print(res)
        plus_operations.append(res)
    elif symbol == "-":
        res = str(a) + " - " + str(b) + " = " + str(a - b)
        print(res)
        minus_operations.append(res)
    elif symbol == "*":
        res = str(a) + " * " + str(b) + " = " + str(a * b)
        print(res)
        con_operations.append(res)
    elif symbol == "/":
        res = str(a) + " / " + str(b) + " = " + str(a / b)
        print(res)
        div_operations.append(res)
    else:
        print("Неверно введена операция, повторите")

    print("+ " + str(plus_operations))
    print("- " + str(minus_operations))
    print("* " + str(con_operations))
    print("/ " + str(div_operations))



