list = []
counter = 0
times_to_loop = 10

while counter < times_to_loop:
    list.append(int(input(">> ")))
    counter += 1

odds = []

for item in list:
    if item % 2 != 0:
        odds.append(item)

if len(odds) != 0:  
    print(max(odds))
else:
    print("No Odd Number Here")