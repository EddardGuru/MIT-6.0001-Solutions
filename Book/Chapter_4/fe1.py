# Finger exercise: Use the find_root function in Figure 4-3 to print
# the sum of approximations to the square root of 25, the cube root of
# -8, and the fourth root of 16. Use 0.001 as epsilon.

def find_root(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

operand_1 = find_root(25, 2, 0.001)
operand_2 = find_root(-8, 3, 0.001)
operand_3 = find_root(16, 4, 0.001)
print(operand_1 + operand_2 + operand_3)