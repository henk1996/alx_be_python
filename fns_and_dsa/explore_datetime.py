from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date(days_to_add):
    future_date = datetime.today() + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

user_input = int(input("Enter the number of days to add to the current date: "))

current_datetime = display_current_datetime()
future_calculated_date = calculate_future_date(user_input)

print(current_datetime)
print(future_calculated_date)
