def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print(f"Addition: {add(x, y)}")
print(f"Subtraction: {subtract(x, y)}")
print(f"Multiplication: {multiply(x, y)}")
print(f"Division: {divide(x, y)}")
