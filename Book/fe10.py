# Finger exercise: The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.

from math import ceil

def solution(num_of_floors):
    is_egg_breaked = True
    low = 0
    high = num_of_floors
    number_of_throwing_egg = 0
    floor = num_of_floors // 2 
    while floor < num_of_floors and floor > 1:
        print(floor)
        if is_egg_breaked:
            high = floor
        else:
            low = floor 
        floor = ceil((high + low) / 2)
        number_of_throwing_egg += 1
    return number_of_throwing_egg + 1

def solutionTwo(total_floors):
    # Initialize the range for binary search
    low, high = 1, total_floors
    eggs_used = 0

    while low <= high:
        # Calculate the midpoint of the current range
        mid = (low + high) // 2
        eggs_used += 1

        # Drop an egg from the midpoint floor
        if mid == total_floors:
            # If the egg doesn't break, we've found the highest floor
            return eggs_used
        elif mid < total_floors:
            # If the egg doesn't break, move to the upper half
            low = mid + 1
        else:
            # If the egg breaks, move to the lower half
            high = mid - 1

    # At this point, we've found the highest safe floor
    return eggs_used

total_floors = 102
eggs_needed = solutionTwo(total_floors)
print(f"At worst, {eggs_needed} eggs are needed to find the highest safe floor.")
print(f">>>>>>   {solution(102)}   <<<<<<<<")