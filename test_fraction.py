import pytest
from fraction import Fraction


def test_initialization() -> None:
    """Test that a Fraction object is initialized correctly."""
    fraction = Fraction(1, 2)

    assert isinstance(fraction, Fraction)
    assert fraction.numerator == 1
    assert fraction.denominator == 2


def test_read_only() -> None:
    """Test that fraction properties cannot be modified."""
    fraction = Fraction(1, 2)

    with pytest.raises(AttributeError):
        fraction.numerator = 3

    with pytest.raises(AttributeError):
        fraction.denominator = 4


def test_invalid_types() -> None:
    """Test that numerator and denominator must be integers."""
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    with pytest.raises(TypeError):
        Fraction(1, 2.5)

    with pytest.raises(TypeError):
        Fraction("1", 2)


def test_invalid_denominator() -> None:
    """Test that the denominator must be positive."""
    with pytest.raises(ValueError):
        Fraction(1, 0)

    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_string_representation() -> None:
    """Test the string and representation methods."""
    fraction = Fraction(1, 2)

    assert str(fraction) == "1/2"
    assert repr(fraction) == "Fraction(1, 2)"


def test_equality() -> None:
    """Test equality and inequality between fractions."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 4)
    fraction3 = Fraction(3, 4)

    assert fraction1 == fraction2
    assert fraction1 != fraction3
    assert not (fraction1 == fraction3)


def test_comparisons() -> None:
    """Test all ordering comparisons between fractions."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 4)
    fraction3 = Fraction(3, 4)

    assert fraction1 < fraction3
    assert fraction1 <= fraction2
    assert fraction3 > fraction1
    assert fraction3 >= fraction2


def test_arithmetic_operations() -> None:
    """Test addition, subtraction, multiplication and division."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)

    assert str(fraction1 + fraction2) == "10/8"
    assert str(fraction1 - fraction2) == "-2/8"
    assert str(fraction1 * fraction2) == "3/8"
    assert str(fraction1 / fraction2) == "4/6"


def test_negative_division() -> None:
    """Test division by a negative fraction."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(-1, 3)

    result = fraction1 / fraction2

    assert str(result) == "-3/2"
    assert result.denominator > 0


def test_division_by_zero() -> None:
    """Test that division by a zero fraction raises an error."""
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(0, 3)

    with pytest.raises(ZeroDivisionError):
        fraction1 / fraction2
