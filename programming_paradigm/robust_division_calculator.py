def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        if numerator != float(numerator) or denominator != float(denominator):
            raise ValueError
        else:
            print(f"The result of the division is {numerator / denominator }")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")