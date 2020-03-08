# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 6 Assignment

class convertKelvinToCelsius:
  def convert(self,value):
    return value-273.15

class convertCelsiusToFahrenheit:
  def convert(self,value):
    return value*1.8+32

class convertKelvinToFahrenheit:
  def convert(self,value):
    return value*1.8-459.67

ktc = convertKelvinToCelsius()
result = ktc.convert(400)
#print (result)

ctf = convertCelsiusToFahrenheit()
result = ctf.convert(126.85)
#print (result)

ktf = convertKelvinToFahrenheit()
result = ktf.convert(126.85)
#print (result)


# Kelvin To Celsius
def convertKelvinToCelsius(a=float):
    """Converts Kelvin to Celsius.

Args:
    a (float): The first parameter.

Returns:
    Numerical Temperature in Celsius.

Examples:
    >>> convertKelvinToCelsius(12)
    '-261.15'

    >>> convertKelvinToCelsius(13)
    '260.15'
    """
    ktc = a - 273.15
    return (ktc)

# Celsius_To_Kelvin
def convertCelsiusToKelvin(b=float):
    """Converts Celsius to Kelvin.

Args:
    b (float): The first parameter.

Returns:
    Temperature in Kelvin.

Examples:
    >>> convertCelsiusToKelvin(12)
    '285.15'

    >>> convertCelsiusToKelvin(13)
    '286.15'
    """
    ctk = b + 273.15
    return (ctk)

# Celsius_To_Fahrenheit
def convertCelsiusToFahrenheit(c=float):
    """Converts Celsius to Fahrenheit.

Args:
    c (float): The first parameter.

Returns:
    Temperature in Fahrenheit.

Examples:
    >>> convertCelsiusToFahrenheit(12)
    '53.6'

    >>> convertCelsiusToFahrenheit(13)
    ' 55.400000000000006'
    """
    ctf = (c*1.8) + 32
    return (ctf)

# Fahrenheit_To_Celsius
def convertFahrenheitToCelsius(d=float):
    """Converts Fahrenheit to Celsius.

Args:
    d (float): The first parameter.

Returns:
    Temperature in Celsius.

Examples:
    >>> convertFahrenheitToCelsius(90)
    '104.4'

    >>> convertFahrenheitToCelsius(95)
    '113.4'
    """
    ftc = (d-32) * 1.8
    return (ftc)

# Kelvin_To_Fahrenheit
def convertKelvinToFahrenheit(e=float):
    """Converts Kelvin to Fahrenheit.

Args:
    e (float): The first parameter.

Returns:
    Temperature in Fahrenheit.

Examples:
    >>> convertKelvinToFahrenheit(100)
    ' -279.66999999999996'

    >>> convertKelvinToFahrenheit(130)
    ' -225.66999999999996'
    """
    ktf = (e-273.15) * 1.8 + 32
    return (ktf)

# Fahrenheit_To_Kelvin
def convertFahrenheitToKelvin(f=float):
    """Converts Fahrenheit to Kelvin.

Args:
    f (float): The first parameter.

Returns:
    Temperature in Kelvin.

Examples:
    >>> convertFahrenheitToKelvin(92)
    ' 381.15'

    >>> convertFahrenheitToKelvin(81)
    ' 361.34999999999997'
    """
    ftk = (f-32) * 1.8 + 273.15
    return (ftk)

#Conversion between miles, yards, and meters
class convertMilesToYards:
  def convert(self,value):
    return value*1760

class convertMilesToMeters:
  def convert(self,value):
    return value*1609.34

class convertYardsToMeters:
  def convert(self,value):
    return value/1.094

mty = convertMilesToYards()
result = mty.convert(400)
#print (result)

mtm = convertMilesToMeters()
result = mtm.convert(126.85)
#print (result)

ytm = convertYardsToMeters()
result = ytm.convert(126.85)
#print (result)

# Miles To Yards
def convertMilesToYards(g=float):
    """Converts Miles To Yards.

Args:
    a (float): The first parameter.

Returns:
    Numerical Conversion of Miles To Yards.

Examples:
    >>> convertMilesToYards(1.0)
    '1760'

    >>> convertMilesToYards(2)
    '3520'
    """
    mty = g * 1760
    return (mty)

# Yards To Miles
def convertYardsToMiles(h=float):
    """Converts Yards To Miles.

Args:
    b (float): The first parameter.

Returns:
    Numerical Conversion of Yards To Miles.

Examples:
    >>> convertYardsToMiles(12)
    '0.00681818'

    >>> convertYardsToMiles(13)
    '0.00738636'
    """
    ytm = h / 1760
    return (ytm)

# Miles To Meters
def convertMilesToMeters(i=float):
    """Converts Miles To Meters.

Args:
    c (float): The first parameter.

Returns:
    Numerical Conversion of Miles To Meters.

Examples:
    >>> convertMilesToMeters(12)
    '19312.1'

    >>> convertMilesToMeters(13)
    '20921.5'
    """
    mitm = i * 1609.34
    return (mitm)

# Meters To Miles
def convertMetersToMiles(j=float):
    """Converts Meters To Miles.

Args:
    d (float): The first parameter.

Returns:
    Numerical Conversion of Meters to Miles.

Examples:
    >>> convertMetersToMiles(90)
    '0.0559234'

    >>> convertMetersToMiles(95)
    """
    metm = j / 1609.34
    return (metm)

# Yards To Meters
def convertYardsToMeters(k=float):
    """Converts Yards To Meters.

Args:
    e (float): The first parameter.

Returns:
    Numerical Conversion of Yards To Meters.

Examples:
    >>> convertYardsToMeters(100)
    '91.44'

    >>> convertYardsToMeters(130)
    '118.872'
    """
    ytm = k / 1.094
    return (ytm)

# Meters to Yards
def convertMeterstoYards(l=float):
    """Converts Meters to Yards.

Args:
    f (float): The first parameter.

Returns:
    Numerical Conversion of Meters to Yards.

Examples:
    >>> convertMeterstoYards(92)
    '100.612'

    >>> convertMeterstoYards(81)
    '88.5827'
    """
    mty = l * 1.094
    return (mty)

#Me testing with print statments
#convertFahrenheit_To_Kelvin(92)
#convertKelvinToCelsius(12)
#convertMeterstoYards(92)

# if __name__ == "__main__":
#     main()
