from typing import Iterable, Tuple


def convert_fahrenheit_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.
    """
    #round to max 2 digit restriction on float
    return round((fahrenheit_temp - 32.0) / 1.80, 2)

def convert_kelvin_to_celsius(kelvin_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in kelvin.
    """
    # Celsius = Kelvin - 273.15
    return  round(kelvin_temp - 273.15, 2)
  

def convert_celsius_to_fahrenheit(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.
    """
    return round((celsius_temp * 1.8) + 32, 2)

def convert_kelvin_to_fahrenheit(kelvin_temp: float) -> float:
    """
    Given a float representing a temperature in kelvin, return the corresponding value in fahrenheit.
    """
    # Fahrenheit = ((Kelvin - 273.15) * 1.8) + 32
    return  round(((kelvin_temp - 273.15) * 1.8) + 32, 2)


def convert_celsius_to_kelvin(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the the corresponding value in kelvin
    """
    return round(celsius_temp + 273.15, 2)
    

def convert_fahrenheit_to_kelvin(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the the corresponding value in kelvin
    """
    return round(((fahrenheit_temp -32) / 1.79999999) + 273.15, 2)
    
   

def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str, output_unit: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.
    """

    # Setup a list to add tuples to as constructed, know length of list for iterations
    tList = []
    tempLen = len(temperatures)
    
    # Check if the input unit of measurement is c or f.  celsius or fahrenheit.
    # Call the functions defined to get the 2nd value for each tuple
    
    # There has got to be a simpler way to code this
    # Method to extract:   def convert_units(list, input unit, output unit)
    if input_unit_of_measurement == 'f' and output_unit == 'c':
        for i in range(0, tempLen):
            cTemp = convert_fahrenheit_to_celsius(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)
    elif input_unit_of_measurement == 'f' and output_unit == 'k':
        for i in range(0, tempLen):
            cTemp = convert_fahrenheit_to_kelvin(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)        
    elif input_unit_of_measurement == 'c' and output_unit == 'k':
        for i in range(0, tempLen):
            cTemp = convert_celsius_to_kelvin(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)     
    elif input_unit_of_measurement == 'c' and output_unit == 'f':
        for i in range(0, tempLen):
            fTemp = convert_celsius_to_fahrenheit(temperatures[i])
            tTemp = temperatures[i], fTemp
            tList.append(tTemp)
    elif input_unit_of_measurement == 'k' and output_unit == 'c':
        for i in range(0, tempLen):
            cTemp = convert_kelvin_to_celsius(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)     
    elif input_unit_of_measurement == 'k' and output_unit == 'f':
        for i in range(0, tempLen):
            cTemp = convert_kelvin_to_fahrenheit(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)     
    
    tempsTuple = tuple(tList)
    return tempsTuple
        
  
