
import pytest
from temperature import Temperature


def test_initialization() -> None:
    """Test that a Temperature object is initialized with default values."""
    temp = Temperature()

    assert isinstance(temp, Temperature)
    assert temp.value == 0.0
    assert temp.unit == 'C'


def test_lowercase_unit() -> None:
    """Test that lowercase temperature units are converted to uppercase."""
    temp = Temperature(25, 'c')
    assert temp.unit == 'C'


def test_read_only() -> None:
    """Test that temperature properties cannot be modified."""
    temp = Temperature(25, 'C')

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = 'F'


def test_invalid_unit() -> None:
    """Test that an invalid temperature unit raises ValueError."""
    with pytest.raises(ValueError):
        Temperature(25, 'X')


def test_below_absolute_zero() -> None:
    """Test that temperatures below absolute zero raise ValueError."""
    with pytest.raises(ValueError):
        Temperature(-274, 'C')

    with pytest.raises(ValueError):
        Temperature(-460, 'F')

    with pytest.raises(ValueError):
        Temperature(-1, 'K')


def test_conversions() -> None:
    """Test conversion between Celsius, Fahrenheit and Kelvin."""
    temp = Temperature(0, 'C')

    assert temp.to_fahrenheit() == 32
    assert temp.to_kelvin() == 273.15

    temp = Temperature(32, 'F')
    assert temp.to_celsius() == 0

    temp = Temperature(273.15, 'K')
    assert temp.to_celsius() == 0


def test_convert_to() -> None:
    """Test conversion to a new Temperature object."""
    temp = Temperature(0, 'C')

    converted = temp.convert_to('F')

    assert isinstance(converted, Temperature)
    assert converted.value == 32
    assert converted.unit == 'F'

    # Check that the original object is unchanged.
    assert temp.value == 0
    assert temp.unit == 'C'


def test_roundtrip_conversion() -> None:
    """Test that converting between units and back preserves the value."""
    original = Temperature(25, 'C')

    converted = original.convert_to('F').convert_to('K').convert_to('C')

    assert converted.value == pytest.approx(25, abs=1e-9)
    assert converted.unit == 'C'


def test_invalid_conversion_unit() -> None:
    """Test that converting to an invalid unit raises ValueError."""
    temp = Temperature(25, 'C')

    with pytest.raises(ValueError):
        temp.convert_to('X')


def test_comparisons() -> None:
    """Test equality and ordering comparisons between temperatures."""
    temp1 = Temperature(0, 'C')
    temp2 = Temperature(32, 'F')
    temp3 = Temperature(100, 'C')

    assert temp1 == temp2
    assert temp1 <= temp2
    assert temp1 >= temp2

    assert temp1 < temp3
    assert temp1 <= temp3
    assert temp3 > temp1
    assert temp3 >= temp1

    assert temp1 != temp3


def test_string_representation() -> None:
    """Test the string and representation methods."""
    temp = Temperature(25, 'C')

    assert str(temp) == "25.00 °C"
    assert repr(temp) == "Temperature(value=25, unit='C')"


def test_reference_points() -> None:
    """Test conversions using known reference temperatures."""

    # Absolute zero
    temp = Temperature(0, 'K')
    assert temp.to_celsius() == pytest.approx(-273.15)
    assert temp.to_fahrenheit() == pytest.approx(-459.67)

    # Freezing point of water
    temp = Temperature(0, 'C')
    assert temp.to_fahrenheit() == pytest.approx(32)

    # Boiling point of water
    temp = Temperature(100, 'C')
    assert temp.to_fahrenheit() == pytest.approx(212)

    # Normal body temperature
    temp = Temperature(37, 'C')
    assert temp.to_fahrenheit() == pytest.approx(98.6)

    # Celsius and Fahrenheit crossover
    temp = Temperature(-40, 'C')
    assert temp.to_fahrenheit() == pytest.approx(-40)
