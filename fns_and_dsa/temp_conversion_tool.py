FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * float(FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * float(CELSIUS_TO_FAHRENHEIT_FACTOR)) + 32


user_input = input("Enter the temperature to convert: ")

if user_input.isdigit():
    temperature = float(user_input)
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    match temp_unit:
        case "c":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {result:.1f}°F")
        case "f":
            result = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {result:.1f}°C")
        case _:
            print("Please enter a valid unit: 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")



