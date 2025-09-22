import math

def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b): 
    return a / b if b != 0 else "You cant Divide by zero"
def power(a, b):
    return a ** b
def square_root(a):
    return math.sqrt(a) if a > 0 else "Square root is negative"