import math

def add(a, b): 
    try:
        return a + b
    except Exception as e:
        return f"error: {e}"

def subtract(a, b):
    try:
        return a - b
    except Exception as e:
        return f"Error: {e}"

def multiply(a, b):
    try:
        return a * b
    except Exception as e:
        return f"Error: {e}"

def divide(a, b):
    try:
        if b == 0:
            return "Error: Division by zero"
        return a / b
    except Exception as e:
        return f"Error: {e}"

def power(a, b):
    try:
        return a ** b
    except Exception as e:
        return f"Error: {e}"

def square_root(a):
    try:
        if a < 0:
            return "Error: Cannot take square root of negative number"
        return math.sqrt(a)
    except Exception as e:
        return f"Error: {e}"