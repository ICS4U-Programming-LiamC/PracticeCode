biggestNum = 0
for attempt in range(1, 11):
    testrange = attempt * 10
    for i in range(999 - testrange, 1010 - testrange):
        for x in range(900, 999):
            num = x * i
            numStr = str(num)
            if (num == int(numStr[::-1])):
                if (num > biggestNum):
                    biggestNum = num
                print(biggestNum)