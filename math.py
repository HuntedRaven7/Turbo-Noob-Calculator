# HI NEO HOW DID I DO (If you aren't Neo then don't worry)
numb1 = float(input("Enter the First Number: "))
numb2 = float(input("Now the Second Number: "))

operator = input("Enter an operation (+, -, *, /): ")

if operator == "+":
    result = numb1 + numb2
    print(f"Result: {result}")
elif operator == "-":
    result = numb1 - numb2
    print(f"Result: {result}")
elif operator == "*":
    result = numb1 * numb2
    print(f"Result: {result}")
elif operator == "/":
    result = numb1 / numb2
    print(f"Result: {result}")