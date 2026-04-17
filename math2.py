def Func():
    num1 = float(input("Give the first number: "))
    op = (input("Give the operator "'/, *, +, -,'": "))
    num2 = float(input("Give the Second number: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2

        print(result)

Func()

