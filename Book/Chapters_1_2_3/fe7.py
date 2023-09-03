# Finger exercise: Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect

import math 

def solutionOne(num):
    if (num == 1):
        return (1, 2)

    guess = 2
    while guess < int(math.sqrt(num)) + 1:
        for i in range(2, 6):
            if (guess ** i == num):
                return (guess, i)
        guess += 1
    return (0, 0)

def solutionTwo(num):
    if (num < 0):
        return None
    for power in range(2, 6):
        root = int(num ** (1/power))
        if root ** power == num:
            return (root, power)
    return None

while True:
    num = int(input(">> "))
    res = solutionTwo(num)
    if res:
        (root, power) = res
        print(f"Root = {root}, Power = {power}")
    else:
        print("No Solution") 
