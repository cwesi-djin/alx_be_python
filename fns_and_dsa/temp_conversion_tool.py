FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {result}°C")

def convert_to_fahrenheit(celsius):
    result = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    print(f"{celsius}°F is {result}°C")

while True:
    tempurature = int(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == 'F':
        convert_to_celsius(tempurature)
        break
    elif unit == 'C':
        convert_to_fahrenheit(tempurature)
        break
    else:
        print("Invalid temperature.")