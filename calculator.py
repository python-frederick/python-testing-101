import numbers


class CalculatorError(Exception):
    """For calculator errors"""


class Calculator:
    """A terrible calculator."""

    def add(self, a, b):
        """Add two numbers."""
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers."""
        return a / b

    def _check_operand(self, operand):
        """Check that the operand is a number."""
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number.')
