import calculator


print("Available operations: add, subtract, multiply, divide, power, square root")

operation = input("Enter operation: ").lower()

if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == 'add':
        result = calculator.add(a, b)
    elif operation == 'subtract':
        result = calculator.subtract(a, b)
    elif operation == 'multiply':
        result = calculator.multiply(a, b)
    elif operation == 'divide':
        result = calculator.divide(a, b)
    elif operation == 'power':
        result = calculator.power(a, b)

elif operation == 'square root':
    a = float(input("Enter a number: "))
    result = calculator.square_root(a)
else:
    result = "Unknown operation"

print("Result:", result)