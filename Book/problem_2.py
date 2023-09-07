list = [2]

# prime_numbers = [[x for x in range(2, 100, 2) if all(x % y != 0 for y in range(3, x))]]
prime_numbers = [x for x in range(2, 100) if all(x % y != 0 for y in range(3, x))]


for i in range(3, 100, 2):
    cond = True
    for itr in range(3, i, 2):
        if i % itr == 0:
            cond = False
            continue
    if cond:
        list.append(i)

print(list)
print(prime_numbers)