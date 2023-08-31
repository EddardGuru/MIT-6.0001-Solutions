import math

annaul_salary = float(input("Annaul Salary >> "))
portion_saved = float(input("Portion Saved >> "))
total_cost = float(input("Total Cost >> "))
semi_annaul_salary = float(input("Semi Annaul Salar >> "))

portion_down_payment = 0.25
current_savings = 0.0
annaul_return = 0.04
month_count = 0

down_payment = total_cost * portion_down_payment

while (current_savings < down_payment):
    month_count += 1
    current_savings += (current_savings * annaul_return) / 12
    current_savings += (annaul_salary / 12) * portion_saved
    if (month_count % 6 == 0):
        annaul_salary += annaul_salary * semi_annaul_salary

print (month_count)
