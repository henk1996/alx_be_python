# Ask user to input financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating Monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

# Calculating annual projected savings
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# checking float monthlly saving equals with integer monthly saving to adjust decimal
if monthly_savings == int(monthly_savings):
    print (f"Your monthly savings are ${int(monthly_savings)}.")
else:
   print (f"Your monthly savings are ${monthly_savings}")
#checking float annual saving is equal with integer monthly annual saving to adjust decimal
if projected_savings == int(projected_savings):
    print (f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
else:
   print (f"Projected savings after one year, with interest, is: ${projected_savings}.")
