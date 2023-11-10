import unittest
import temperature_utils2


class TemperatureUtils2Test(unittest.TestCase):

    def test_convert_fahrenheit_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_fahrenheit_to_celsius(temp_in))

    def test_convert_celsius_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_celsius_to_fahrenheit(temp_in))

    def test_convert_kelvin_to_fahrenheit(self):
        test_cases = [
            (343, 157.73),
            (0, -459.67),
            (273.15, 32)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_kelvin_to_fahrenheit(temp_in))

    def test_convert_kelvin_to_celsius(self):
        test_cases = [
            (200, -73.15),
            (0, -273.15),
            (273.15, 0),
            (500, 226.85)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_kelvin_to_celsius(temp_in))

    def test_convert_celsius_to_kelvin(self):
        test_cases = [
            (100, 373.15),
            (0, 273.15),
            (-5, 268.15),
            (-273.15, 0)
            
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_celsius_to_kelvin(temp_in))

    def test_convert_fahrenheit_to_kelvin(self):
        test_cases = [
            (242, 389.82),
            (0, 255.37),
            (98.6, 310.15),
            (32, 273.15)
            
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils2.convert_fahrenheit_to_kelvin(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils2.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils2.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils2.temperature_tuple(temps_input, "a"))
