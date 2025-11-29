def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y if y != 0 else "Cannot divide by Zero!"


while True:
    num1 = float(input("First Number "))
    num2 = float(input("Second Number "))
    operation = input("Choose Operation +, -, *, / ")
    result = 0

    if operation == "+":
        result = add(num1, num2)
        print(f"The result is: {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"The result is: {result}")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"The result is: {result}")
    elif operation == "/":
        if num2 != 0:
            result = divide(num1, num2)
            print(f"The result is: {result}")
        else:
            print("ERROR: Cannot divide by Zero! ")
    else:
        print("Invalid Input")
    again = input("Do you want to continue y/n  ")
    if again == "n":
        break
    else:
        continue
