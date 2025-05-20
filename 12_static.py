class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")