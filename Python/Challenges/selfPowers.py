total = 0
for x in range(1, 1000+1):
    total = total + x**x

counter = 0
while (counter < 10):
    print(str(total)[::-1])
    counter += 1