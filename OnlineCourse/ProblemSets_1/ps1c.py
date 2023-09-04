def down_payment_price(down_payment, house_price):
    return down_payment * house_price

def monthly_salary(annual_salary):
    return annual_salary / 12

def monthly_return(current_savings, annaul_return):
    return (current_savings * annaul_return) / 12

def saved(annual_salary, porition_saved):
    return (annual_salary / 12) * porition_saved

def raise_salary(annual_salary, semi_annual_salary):
    return annual_salary * semi_annual_raise

def calculate(semi_annual_raise, annual_return, months, annual_salary, porition_saved):
    current_savings = 0.0
    for month in range(1, months + 1):
        current_savings += monthly_return(current_savings, annual_return)
        current_savings += saved(annual_salary, porition_saved)
        if (month % 6 == 0):
            annual_salary += raise_salary(annual_salary, semi_annual_raise)
    return current_savings

semi_annual_raise = 0.07
annual_return = 0.04
down_payment = 0.25
house_cost = 1000000
months = 36
low_boundry = 100

while True:
    annual_salary = int(input(">> "))
    high = 100
    low = 0
    res = 0
    total = down_payment_price(down_payment, house_cost)
    steps = 0
    porition_saved = 0


    while abs(res - total) >= low_boundry and porition_saved < 100:
        steps += 1
        porition_saved = (high + low) / 2
        res = calculate(semi_annual_raise, annual_return, months, annual_salary, porition_saved / 100)
        if (res > total):
            high = porition_saved
        else:
            low = porition_saved

    if (porition_saved >= 100):
        print("Error!!")
    else:
        print(steps)
        print(porition_saved)
