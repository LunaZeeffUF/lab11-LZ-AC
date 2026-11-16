# https://github.com/LunaZeeffUF/lab11-LZ-AC
# Partner 1: Luna Zeeff
# Partner 2: Adolfo Camacho

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def subtract(a, b):
    return a - b

def logarithm(a, b):

    if a <= 0 or a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid argument")
    return math.log(b, a)

def exp(a, b):
    return a**b
