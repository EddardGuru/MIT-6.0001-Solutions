x = int(input("first >> "))
y = int(input("second >> "))
z = int(input("third >> "))

list = [x, y , z]
odds = []

for item in list:
    if item % 2 != 0:
        odds.append(item)

if len(odds) == 0:
    print(min(list))
else:
    print(max(odds))


