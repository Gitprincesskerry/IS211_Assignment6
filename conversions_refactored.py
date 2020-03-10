# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 6 Assignment

import conversions

class ConversionNotPossible(Exception):
    def __init__(self, a):
        print(a)
        pass

def convert(fromUnit, toUnit, value):
        if fromUnit == "Kelvin" and toUnit == "Celsius":
            result = value - 273.15
        elif fromUnit == "Celsius" and toUnit == "Kelvin":
            result = value + 273.15
        elif fromUnit == "Celsius" and toUnit == "Fahrenheit":
            result = (value*1.8) + 32
        elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
            result = (value-32) * 1.8
        elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
            result = (value-273.15) * 1.8 + 32
        elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
            result = (value-32) * 1.8 + 273.15
        elif fromUnit == "Miles" and toUnit == "Yards":
            result = value * 1760.0
        elif fromUnit == "Yards" and toUnit == "Miles":
            result = value / 1760.0
        elif fromUnit == "Miles" and toUnit == "Meters":
            result = value * 1609.34
        elif fromUnit == "Meters" and toUnit == "Miles":
            result = (value / 1609.34)
        elif fromUnit == "Yards" and toUnit == "Meters":
            result = (value / 1.094)
        elif fromUnit == "Meters" and toUnit == "Yards":
            result = value * 1.094
        else:
            raise ConversionNotPossible("Cannot convert temperature to distance method and vice versa, please utilize the appropriate conversion")
        return result
