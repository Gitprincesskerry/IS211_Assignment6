# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 6 Assignment


# Kelvin To Celsius
def convertKelvinToCelsius(a=float):
    """Converts Kelvin to Celsius.

Args:
    a (float): The first parameter.

Returns:
    Numerical Temperature in Celsius.

Examples:
    >>> convertKelvinToCelsius(12.0)
    '-261.15'

    >>> convertKelvinToCelsius(13.0)
    '260.15'
    """
    # if type(a) not in [float]:
    #     raise TypeError("Input must be a float")

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
    >>> convertCelsiusToKelvin(12.0)
    '285.15'

    >>> convertCelsiusToKelvin(15.0)
    '288.15'
    """
    # if type(b) not in [float]:
    #     raise TypeError("Input must be a float")

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
    >>> convertCelsiusToFahrenheit(12.0)
    '53.6'

    >>> convertCelsiusToFahrenheit(13.0)
    ' 55.4'
    """

    # if type(c) not in [float]:
    #     raise TypeError("Input must be a float")

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

    # if type(d) not in [float]:
    #     raise TypeError("Input must be a float")

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
    >>> convertKelvinToFahrenheit(100.0)
    ' -279.67'

    >>> convertKelvinToFahrenheit(130.5)
    ' -224.77'
    """

    # if type(e) not in [float]:
    #     raise TypeError("Input must be a float")

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
    >>> convertFahrenheitToKelvin(92.0)
    ' 381.15'

    >>> convertFahrenheitToKelvin(85.5)
    ' 369.45'
    """

    ftk = (f-32) * 1.8 + 273.15
    return (ftk)

#Conversion between miles, yards, and meters

# Miles To Yards
def convertMilesToYards(g=float):
    """Converts Miles To Yards.

Args:
    a (float): The first parameter.

Returns:
    Numerical Conversion of Miles To Yards.

Examples:
    >>> convertMilesToYards(1.0)
    '1760.0'

    >>> convertMilesToYards(2.0)
    '3520.0'
    """
    mty = g * 1760.0
    return (mty)


# Yards To Miles
def convertYardsToMiles(h=float):
    """Converts Yards To Miles.

Args:
    b (float): The first parameter.

Returns:
    Numerical Conversion of Yards To Miles.

Examples:
    >>> convertYardsToMiles(12.5)
    '0.00710227272727'

    >>> convertYardsToMiles(13.0)
    '0.00738636363636'
    """
    ytm = h / 1760.0
    return (ytm)


# Miles To Meters
def convertMilesToMeters(i=float):
    """Converts Miles To Meters.

Args:
    c (float): The first parameter.

Returns:
    Numerical Conversion of Miles To Meters.

Examples:
    >>> convertMilesToMeters(15.5)
    '24944.77'

    >>> convertMilesToMeters(5.0)
    '8046.7'
    """
    mitm = i * 1609.34
    return(mitm)


# Meters To Miles
def convertMetersToMiles(j=float):
    """Converts Meters To Miles.

Args:
    d (float): The first parameter.

Returns:
    Numerical Conversion of Meters to Miles.

Examples:
    >>> convertMetersToMiles(90.0)
    '0.0559235462985'

    >>> convertMetersToMiles(1008.7)
    '0.626778679459'
    """
    metm = (j / 1609.34)
    return (metm)


# Yards To Meters
def convertYardsToMeters(k=float):
    """Converts Yards To Meters.

Args:
    e (float): The first parameter.

Returns:
    Numerical Conversion of Yards To Meters.

Examples:
    >>> convertYardsToMeters(100.5)
    '91.8647166362'

    >>> convertYardsToMeters(130.2)
    '119.012797075'
    """
    ytm = (k / 1.094)
    return (ytm)

# Meters to Yards
def convertMeterstoYards(l=float):
    """Converts Meters to Yards.

Args:
    f (float): The first parameter.

Returns:
    Numerical Conversion of Meters to Yards.

Examples:
    >>> convertMeterstoYards(92.0)
    '100.648'

    >>> convertMeterstoYards(81.7)
    '89.3798'
    """
    mty = l * 1.094
    return (mty)
