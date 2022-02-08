oldFib = 0
currentFib = 1
newFib = 0
total = 0
while currentFib < 4000000:
    if currentFib % 2 == 0:
        total += currentFib
    else:
        pass
    newFib = oldFib + currentFib
    oldFib = currentFib
    currentFib = newFib

print(total)




