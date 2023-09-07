# Finger exercise: Write a list comprehension that generates all
# non-primes between 2 and 100.
non_prime_numbers = [x for x in range(2, 100) if any(x % y == 0 for y in range(2, x))]
print(non_prime_numbers)