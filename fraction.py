class Fraction:
    """
    A class for representing fractions.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialize a fraction object.

        Args:
            numerator: The numerator of the fraction.
            denominator: The denominator of the fraction.

        Raises:
            TypeError: If numerator or denominator is not an integer.
            ValueError: If the denominator is not positive.
        """

        # Check that numerator and denominator are integers.
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must be integers.")

        # Check that the denominator is positive.
        if denominator <= 0:
            raise ValueError("Denominator must be greater than zero.")

        # Store the numerator and denominator.
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction."""
        return self._denominator

    def __eq__(self, other: object) -> bool:
        """Check if two fractions are equal."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator * other._denominator ==
                other._numerator * self._denominator)

    def __ne__(self, other: object) -> bool:
        """Check if two fractions are not equal."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool:
        """Check if the fraction is less than another fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator * other._denominator <
                other._numerator * self._denominator)

    def __le__(self, other: object) -> bool:
        """Check if the fraction is less than or equal to another."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator * other._denominator <=
                other._numerator * self._denominator)

    def __gt__(self, other: object) -> bool:
        """Check if the fraction is greater than another fraction."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator * other._denominator >
                other._numerator * self._denominator)

    def __ge__(self, other: object) -> bool:
        """Check if the fraction is greater than or equal to another."""
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self._numerator * other._denominator >=
                other._numerator * self._denominator)
    
    def __add__(self, other: object) -> 'Fraction':
        """Add two fractions and return a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the numerator and denominator.
        numerator = (self._numerator * other._denominator +
                     other._numerator * self._denominator)
        denominator = self._denominator * other._denominator

        # Return a new Fraction object.
        return Fraction(numerator, denominator)
    
    def __sub__(self, other: object) -> 'Fraction':
        """Subtract two fractions and return a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculate the numerator and denominator.
        numerator = (self._numerator * other._denominator -
                     other._numerator * self._denominator)
        denominator = self._denominator * other._denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other: object) -> 'Fraction':
        """Multiply two fractions and return a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Multiply the numerators and denominators.
        numerator = self._numerator * other._numerator
        denominator = self._denominator * other._denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other: object) -> 'Fraction':
        """Divide two fractions and return a new Fraction object."""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Check that the divisor is not zero.
        if other._numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")

        # Multiply by the reciprocal of the second fraction.
        numerator = self._numerator * other._denominator
        denominator = self._denominator * other._numerator

        # Ensure the denominator stays positive.
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        """Return a human-readable string of the fraction."""
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self) -> str:
        """Return an unambiguous representation of the fraction."""
        return f"Fraction({self._numerator}, {self._denominator})"
