def celsius_to_fahrenheit_converter(temperature):
    return (temperature * 9 / 5) + 32


def fahrenheit_to_celsius_converter(temperature):
    return (temperature - 32) * 5 / 9


def celsius_to_kelvin_converter(temperature):
    return temperature + 273.15


def fahrenheit_to_kelvin_converter(temperature):
    return (temperature - 32) * 5 / 9 + 273.15
