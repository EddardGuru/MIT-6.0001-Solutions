# Finger exercise: Add some code to the implementation of
# Newton–Raphson that keeps track of the number of iterations used
# to find the root. Use that code as part of a program that compares the
# efficiency of Newton–Raphson and bisection search. (You should
# discover that Newton–Raphson is far more efficient.

def newton_raphson(num):
    epsilon = 0.01
    guess = num / 2
    number_of_operations = 0
    while abs(guess ** 2 - num) >= epsilon:
        number_of_operations += 1
        guess = guess - ((guess ** 2 - num ) / (2 * guess))
    return (guess, number_of_operations)

while True:
    num = int(input(">> "))
    guess, total = newton_raphson(num)
    print(guess)
    print(total)