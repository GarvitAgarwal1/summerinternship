num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

while True:
    print("SIMPLE CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Exit")

    val = int(input("Enter your choice (1–6): "))

    if val == 1:
        print(f"Addition: {num1} + {num2} = {num1 + num2}")
    elif val == 2:
        print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    elif val == 3:
        print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    elif val == 4:
        if num2 != 0:
            print(f"Division: {num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero")
    elif val == 5:
        if num2 != 0:
            print(f"Modulo: {num1} % {num2} = {num1 % num2}")
        else:
            print("Cannot find modulo by zero")
    elif val == 6:
        print("Exiting the calculator.")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 6.")
