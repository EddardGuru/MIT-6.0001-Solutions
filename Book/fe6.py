# testing whether an integer is a prime number and returning the largest
#   divisor if it is not

def is_prime(num):
    if (num == 2):
        return (True, 0)
    if (num < 2 or num % 2 == 0):
        return (False, num // 2)

    for i in range(3, num, 2):
        if (num % i == 0):
            return (False, num // i)
    return (True, 0)

while True:
    x  = int(input(">> "))
    (is_prime_number, largest_divisor) = is_prime(x)
    if (is_prime_number):
        print("Prime")
    else:
        print(largest_divisor)

