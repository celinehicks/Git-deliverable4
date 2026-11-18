
import math
from types import NotImplementedType

class Temperature:
    """
     A class for representing temperatures in Celsius, Fahrenheit and Kelvin.
    """    
    def __init__(self, value: float = 0.0, unit: str =  'C')-> None:
        """
            Initialize a temperature object.
        
            Args:
                value: The numerical temperature value.
                unit: The temperature unit (C, F or K).
                          Defaults to Celsius.
        
            Raises:
                ValueError: If the unit is invalid or the
                            temperature is below absolute zero.
        """
        # Store the temperature value and normalize the unit.
        self._value = value
        self._unit = unit.upper()

        # Check that the temperature unit is valid.
        valid_units = ['C', 'F', 'K']
        if self._unit not in valid_units:
            raise ValueError(f"Invalid unit '{self._unit}'. Valid units are: {', '.join(valid_units)}.")
        
        # Check that the temperature is not below absolute zero.
        if self._unit == 'C' and self._value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
        elif self._unit == 'F' and self._value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
        elif self._unit == 'K' and self._value < 0:
            raise ValueError("Temperature cannot be below absolute zero (0 K).")

    @property
    def value(self)-> float:
        """Return the numerical temperature value."""
        return self._value
    @property
    def unit(self)-> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self)-> float:
        """Convert the temperature to Celsius."""
        if self._unit == 'C':
            return self._value
        elif self._unit == 'F':
            return (self._value - 32) * 5.0 / 9.0
        elif self._unit == 'K':
            return self._value - 273.15
       

    def to_fahrenheit(self)-> float:
        """Convert the temperature to Fahrenheit."""
        if self._unit == 'C':
            return (self._value * 9.0 / 5.0) + 32
        elif self._unit == 'F':
            return self._value
        elif self._unit == 'K':
            return (self._value - 273.15) * 9.0 / 5.0 + 32
   

    def to_kelvin(self)-> float:
        """Convert the temperature to Kelvin."""
        if self._unit == 'C':
            return self._value + 273.15
        elif self._unit == 'F':
            return (self._value - 32) * 5.0 / 9.0 + 273.15
        elif self._unit == 'K':
            return self._value

    def convert_to(self, new_unit: str) -> 'Temperature':
        """
        Convert the temperature to a new unit.

        Args:
            new_unit: The unit to convert to (C, F or K).

        Returns:
            A new Temperature object in the requested unit.

        Raises:
            ValueError: If the requested unit is invalid.
        """

        new_unit = new_unit.upper()
        # Validate the requested unit.
        if new_unit not in ['C', 'F', 'K']:
            raise ValueError(f"Invalid unit '{new_unit}'. Valid units are: C, F, K.")

        # Return a new Temperature object in the requested unit.
        if new_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        elif new_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        elif new_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')
        
    def __eq__(self, other: object)-> bool:
        """Check if two temperatures are equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return math.isclose(
                self.to_celsius(),
                other.to_celsius(),
                rel_tol=1e-9,
                abs_tol=1e-9
            )
    
    def __ne__(self, other: object)-> bool:
        """Check if two temperatures are not equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return not math.isclose(
            self.to_celsius(),
            other.to_celsius(),
            rel_tol=1e-9,
            abs_tol=1e-9
        )
    
    def __lt__(self, other: object)-> bool:
        """Check if the temperature is less than another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() < other.to_celsius()

    def __le__(self, other: object)-> bool:
        """Check if the temperature is less than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() <= other.to_celsius()

    def __gt__(self, other: object)-> bool:
        """Check if the temperature is greater than another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() > other.to_celsius()

    def __ge__(self, other: object)-> bool:
        """Check if the temperature is greater than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() >= other.to_celsius()
    


    def __str__(self)-> str:
        """Return a readable string with two decimal places."""
        return f"{self._value:.2f} °{self._unit}"
    
    def __repr__(self)-> str:
        """Return a string representation of the Temperature object."""
        return f"Temperature(value={self._value}, unit='{self._unit}')"

