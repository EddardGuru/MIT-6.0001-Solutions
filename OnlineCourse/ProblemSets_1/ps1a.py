import math

annaul_salary = float(input("Annaul Salary >> "))
portion_saved = float(input("Portion Saved >> "))
total_cost = float(input("Total Cost >> "))

portion_down_payment = 0.25
current_savings = 0.0
monthly_salary = annaul_salary / 12
annaul_return = 0.04
month_count = 0

down_payment = total_cost * portion_down_payment

while (current_savings < down_payment):
    month_count += 1
    current_savings += (current_savings * annaul_return) / 12
    current_savings += monthly_salary * portion_saved

print (month_count)
