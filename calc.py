plus_operations = []
minus_operations = []
multiplication_operations = []
division_operations = []

while True:
    var1 = int(input())
    var2 = int(input())
    symbol = input()

    if symbol == "+":
        res = str(var1) + " + " + str(var2) + " = " + str(var1+var2)
        print(res)
        plus_operations.append(res)
    elif symbol == "-":
        res = str(var1) + " - " + str(var2) + " = " + str(var1 - var2)
        print(res)
        minus_operations.append(res)
    elif symbol == "*":
        res = str(var1) + " * " + str(var2) + " = " + str(var1 * var2)
        print(res)
        multiplication_operations.append(res)
    elif symbol == "/":
        res = str(var1) + " / " + str(var2) + " = " + str(var1 / var2)
        print(res)
        division_operations.append(res)
    else:
        print("Неверно введена операция, повторите")

    print("+ " + str(plus_operations))
    print("- " + str(minus_operations))
    print("* " + str(multiplication_operations))
    print("/ " + str(division_operations))
