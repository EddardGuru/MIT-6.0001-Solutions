def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    sum = 0
    for x in map(lambda x, y: x ** y, L1, L2):
        sum += x
    return sum

L1 = [1, 2, 99]
L2 = [2, 3, 0]
print(f(L1, L2))
