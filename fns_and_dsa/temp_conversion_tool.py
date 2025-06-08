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
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    match temp_unit:
        case "c":
            result = convert_to_fahrenheit(float(user_input))
            print (result)
        case "f":
            result = convert_to_celsius(float(user_input))
            print (result)
        case _:
            print("enters a valid temperature and unit.")
else:
    print("Invalid temperature. Please enter a numeric value.")



