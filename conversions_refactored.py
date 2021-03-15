
def convert(fromUnit, toUnit, value):
    """
    Convert
    """
    if fromUnit == toUnit:
        return value
    elif fromUnit == "C" and toUnit == "K":
        # do Celsius to Kelvin
        value = value + 273.15
        return value
    elif fromUnit == "C" and toUnit == "F":
        # do Celsius to Fahrenheit
        value = value * 9/5 + 32
        return value
    elif fromUnit == "K" and toUnit == "C":
        # do Kelvin to Celsius
        value = value - 273.15
        return value
    elif fromUnit == "K" and toUnit == "F":
        # do Kelvin to Farenheit
        value = value * 9/5 - 459.67
        return value
    elif fromUnit == "F" and toUnit == "K":
        # do Farenheit to Kelvin
        value = (value + 459.67) * 5/9
        return value
    elif fromUnit == "F" and toUnit == "C":
        # do Farenheit to Celsius
        value = (value - 32) * 5/9
        return value
    elif fromUnit == "m" and toUnit == "yd":
        # do meters to yards conversion
        value = value * 1.094
        return value
    elif fromUnit == "m" and toUnit == "mi":
        # do meters to miles conversion
        value = value * 0.000621
        return value
    elif fromUnit == "yd" and toUnit == "m":
        # do yards to meters conversion
        value = value / 1.094
        return value
    elif fromUnit == "yd" and toUnit == "mi":
        # do yards to miles conversion
        value = value / 1760
        return value
    elif fromUnit == "mi" and toUnit == "m":
        # do miles to meters conversion
        value = value * 1609.34
        return value
    elif fromUnit == "mi" and toUnit == "yd":
        # do miles to yards conversion
        value = value * 1760
        return value
    else:
        raise ConversionNotPossible("Incompatible units. Conversion is not possible.")

class ConversionNotPossible(Exception):
    pass
