
def convertCelsiusToKelvin(celsius):
    """
    Converts celsius to kelvin
    """
    kelvin = celsius + 273.15
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def convertKelvinToCelsius(kelvin):
    """
    Converts celsius to kelvin
    """
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    """
    Converts Celsius to Fahrenheit
    """
    fahrenheit = kelvin * 9/5 - 459.67
    return fahrenheit

def convertFahrenheitToKelvin(fahrenheit):
    """
    Converts celsius to kelvin
    """
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def convertFahrenheitToCelsius(fahrenheit):
    """
    Converts Celsius to Fahrenheit
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# def plus2(number):
#     """Returns number + 2"""
#     return number + 2
