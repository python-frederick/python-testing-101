class CalculatorError(Exception):
    """For calculator errors"""


class Calculator:
    """A terrible calculator."""

    def add(self, a, b):
        """Add two numbers."""
        try:
            return a + b
        except TypeError:
            raise CalculatorError("An addend was not a number")

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        return a / b
