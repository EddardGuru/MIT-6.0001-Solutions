# Finger exercise: Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to have a loop that is a primality test nested inside a loop that
# iterates over the odd integers between 3 and 999

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

sum = 0

for num in range(2, 1000):
    if (is_prime(num)):
        sum += num

print(sum)
