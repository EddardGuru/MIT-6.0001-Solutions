# Finger exercise: Use find to implement a function satisfying the
# specification
def find_last(s, sub):
    """s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s"""
    index = s.find(sub)
    if (index == -1):
        return None
    occurances = []
    start = 0
    while index != -1:
        index = s.find(sub, start)
        occurances.append(index)
        start = index + 1
    return occurances

str = "dream of me"
subStr = "e"

res = find_last(str, subStr)
if res:
    print(res[-2])
else:
    print("Error")

