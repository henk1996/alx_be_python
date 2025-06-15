def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError

        result = numerator / denominator
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero.")
    except ValueError:
<<<<<<< HEAD
        return ("Error: Please enter numeric values only.")
=======
        return ("Error: Please enter numeric values only.")
>>>>>>> refs/remotes/origin/main
