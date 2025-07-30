# Simple Calculator Program
# Ask the user for input numbers and operators
a = input("Enter the first number: ")
b = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

# Convert input strings to floats
a = float(a)
b = float(b)

# Perform the operation and print the result
# Addition
if operation == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
    # Subtraction
elif operation == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
    # Multiplication
elif operation == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
# Division
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of: +, -, *, /")
