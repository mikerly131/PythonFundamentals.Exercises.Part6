from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """

    #round to pass test, its 2 digit restriction on float
    return round((fahrenheit_temp - 32.0) / 1.80, 2)
    # remove pass statement and implement me


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    return round((celsius_temp * 1.8) + 32, 2)
    pass  # remove pass statement and implement me


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """

    # Setup a list to add tuples to as constructed, know length of list for iterations
    tList = []
    tempLen = len(temperatures)
    
    # Check if the input unit of measurement is c or f.  celsius or fahrenheit.
    # Call the functions defined to get the 2nd value for each tuple
    if input_unit_of_measurement == 'f':
        for i in range(0, tempLen):
            cTemp = convert_to_celsius(temperatures[i])
            tTemp = temperatures[i], cTemp
            tList.append(tTemp)
    elif input_unit_of_measurement == 'c':
        for i in range(0, tempLen):
            fTemp = convert_to_fahrenheit(temperatures[i])
            tTemp = temperatures[i], fTemp
            tList.append(tTemp)
    
    tempsTuple = tuple(tList)
    return tempsTuple
        
    # remove pass statement and implement me
