
longestChain = 0
for i in range(3, 1000000):
    num = i
    counter = 0
    while(num!=1):
        counter += 1
        if num % 2 == 0:
            num/=2
        else:
            num = num*3 + 1
    if (counter > longestChain):
        print(i)
        longestChain = counter

print(longestChain)