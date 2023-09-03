def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    counter = 3
    while counter < num:
        if num % counter == 0:
            return False
        counter += 2
    return True

sum = 2
counter = 3
upper_bound = 1000
while counter < upper_bound:
    if is_prime(counter):
        sum += counter
    counter += 1

print(sum)