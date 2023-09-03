def log(x, base, epsilon):
    lower_bound = 0
    while base ** lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    ans = (high + low) / 2
    while abs(base ** ans - x) >= epsilon:
        if base ** ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans
