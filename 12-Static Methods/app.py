# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
#°F = (°C × 9/5) + 32
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5)+32
        return f

print(TemperatureConverter.celsius_to_fahrenheit(100),"F")