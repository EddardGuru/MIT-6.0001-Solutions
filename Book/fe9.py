# Finger exercise: What would have to be changed to make the code
# in Figure 3-5 work for finding an approximation to the cube root of
# both negative and positive numbers? Hint: think about changing low
# to ensure that the answer lies within the region being searched.

def foo(num):
    epsilon = 0.01
    guesses, low = 0, 0 
    x = abs(num)
    high = max(1, x)
    ans = (low + high) / 2
    while abs(ans ** 3 - x) >= epsilon:
        if (ans ** 3 > x):
            high = ans
        else:
            low = ans
        ans = (low + high) / 2
        guesses += 1
    if (abs(ans ** 3 - x) < epsilon):
        if (num < 0):
            ans = -ans
        return (ans, guesses)
    else:
        return None

    
while True:
    num = int(input(">> "))
    res = foo(num)
    if res:
        (ans, guesses) = res
        print(f"Answer: {ans}, Gusses: {guesses}")
    else:
        print("Faild")
