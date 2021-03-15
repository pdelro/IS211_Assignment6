import unittest
import conversions
import conversions_refactored


class ConversionFunctions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 300
        expected = 573.15
        actual = conversions.convertCelsiusToKelvin(celsius)

        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to Kelvin conversion failed")


    def test_convertCelsiusToFahrenheit(self):
        celsius = 300
        expected = 572.00
        actual = conversions.convertCelsiusToFahrenheit(celsius)

        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to Fahrenheit conversion failed")


    def test_convertKelvinToCelsius(self):
        kelvin = 300
        expected = 26.85
        actual = conversions.convertKelvinToCelsius(kelvin)

        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Celsius conversion failed")


    def test_convertKelvinToFahrenheit(self):
        kelvin = 300
        expected = 80.33
        actual = conversions.convertKelvinToFahrenheit(kelvin)

        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Fahrenheit conversion failed")


    def test_convertFahrenheitToKelvin(self):
        fahrenheit = 300
        expected = 422.04
        actual = conversions.convertFahrenheitToKelvin(fahrenheit)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Kelvin conversion failed")


    def test_convertFahrenheitToCelsius(self):
        fahrenheit = 300
        expected = 148.89
        actual = conversions.convertFahrenheitToCelsius(fahrenheit)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Celsius conversion failed")


    # def test_plus2(self):
    #     number = 5
    #     expected = 7
    #     actual = conversions.plus2(number)
    #
    #     self.assertEqual(actual, expected, "Numbers don't match...")


    def test_convert(self):
        fromUnit = 'K'
        toUnit = 'K'
        value = 300
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertTrue(actual is value, msg="Conversion of unit to itself failed")


    def test_convertCtoK(self):
        fromUnit = 'C'
        toUnit = 'K'
        value = 300
        expected = 573.15
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to Kelvin conversion failed")


    def test_convertCtoF(self):
        fromUnit = 'C'
        toUnit = 'F'
        value = 300
        expected = 572.00
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to Fahrenheit conversion failed")


    def test_convertKtoC(self):
        fromUnit = 'K'
        toUnit = 'C'
        value = 300
        expected = 26.85
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Celsius conversion failed")


    def test_convertKtoF(self):
        fromUnit = 'K'
        toUnit = 'F'
        value = 300
        expected = 80.33
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Kelvin to Fahrenheit conversion failed")


    def test_convertFtoK(self):
        fromUnit = 'F'
        toUnit = 'K'
        value = 300
        expected = 422.04
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Kelvin conversion failed")


    def test_convertFtoC(self):
        fromUnit = 'F'
        toUnit = 'C'
        value = 300
        expected = 148.89
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Fahrenheit to Celsius conversion failed")


    def test_convertmtoyd(self):
        fromUnit = 'm'
        toUnit = 'yd'
        value = 300
        expected = 328.20
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Meters to yards conversion failed")


    def test_convertmtomi(self):
        fromUnit = 'm'
        toUnit = 'mi'
        value = 300
        expected = 0.19
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Meters to miles conversion failed")


    def test_convertydmtom(self):
        fromUnit = 'yd'
        toUnit = 'm'
        value = 300
        expected = 274.22
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Yards to meters conversion failed")


    def test_convertydtomi(self):
        fromUnit = 'yd'
        toUnit = 'mi'
        value = 300
        expected = 0.17
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Yards to meters conversion failed")


    def test_convertmitom(self):
        fromUnit = 'mi'
        toUnit = 'm'
        value = 300
        expected = 482802.00
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to meters conversion failed")


    def test_convertmitoyd(self):
        fromUnit = 'mi'
        toUnit = 'yd'
        value = 300
        expected = 528000.00
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to yards conversion failed")

if __name__ == '__main__':
    unittest.main()
