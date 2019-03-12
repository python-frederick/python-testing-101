from calculator import Calculator


def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5
