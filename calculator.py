import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("2 * 3 =", multiply(2, 3))
    print("5 / 2 =", divide(5, 2))
    print("2 ^ 3 =", power(2, 3))
    print("5 ^ 0 =", power(5, 0))
    print("/2 =", sqrt(2))
    print("/5 =", sqrt(5))
