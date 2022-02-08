intervalOfPrimes = 1000000
primes = []
listOfPrimes = [2, 3]
for i in range(3, intervalOfPrimes, 2):
    primes.append(i)
print("done list")
while(primes):
    for index, i in enumerate(primes):
        if i % listOfPrimes[-1] == 0:
            primes.pop(index)

    listOfPrimes.append(primes[0])
    primes.pop(0)

for i in range(len(listOfPrimes) - 20, len(listOfPrimes)):
    print(listOfPrimes[i])

print(len(listOfPrimes))