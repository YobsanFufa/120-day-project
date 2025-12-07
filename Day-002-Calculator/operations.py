# ==========================================
# Module: Operations
# ==========================================
# Purpose:
# Defines the mathematical functions used by the calculator.
# Keeping logic separate from the interface makes code testable and reusable.
# ==========================================

import math

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """
    Returns the division of a by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Returns a raised to the power of b."""
    return math.pow(a, b)

def sqrt(a):
    """
    Returns the square root of a.
    Raises ValueError if a is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)
