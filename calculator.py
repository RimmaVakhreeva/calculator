def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y
