monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

if monthly_savings == int(monthly_savings):
    print (f"Your monthly savings are ${int(monthly_savings)}.")
else:
   print (f"Your monthly savings are ${monthly_savings}")
if projected_savings == int(projected_savings):
    print (f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
else:
   print (f"Projected savings after one year, with interest, is: ${projected_savings}.")

