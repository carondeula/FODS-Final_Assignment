def add(a, b):
    """Returns the addition of a and b."""
    return a + b

def subtract(a, b):
    """Returns the subtraction of b from a."""
    return a - b

def multiply(a, b):
    """Returns the multiplication of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b; raises error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def truncated_division(a, b):
    """Returns the truncated (integer) division of a by b; raises error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a // b

def modulus(a, b):
    """Returns the modulus (remainder) of a divided by b; raises error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b

def exponentiation(a, b):
    """Returns a raised to the power of b."""
    return a ** b

if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Addition:", add(a, b))
        print("Subtraction:", subtract(a, b))
        print("Multiplication:", multiply(a, b))
        print("Division:", divide(a, b))
        print("Truncated Division:", truncated_division(a, b))
        print("Modulus:", modulus(a, b))
        print("Exponentiation:", exponentiation(a, b))
    except ValueError as e:
        print("Error:", e)
