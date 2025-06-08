import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def future_date(user_date):
    Futur_date = datetime.datetime.today()
    new_date = int(Futur_date.strftime("%d")) + user_date
    display_date = Futur_date.strftime(f"%Y-%m-{new_date}")
    return display_date


user_input = int(input("Enter the number of days to add to the current date: "))

current_datetime = display_current_datetime()
future_calculated_date = future_date(user_input)

print(current_datetime)
print(future_calculated_date)




