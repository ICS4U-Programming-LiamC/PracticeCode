
import math
biggest_prime = (2000000)
number_of_primes = 1000000
primes = [2, 3]
counter = 0
for number in range(6, biggest_prime + 1, 6):
    # local vars
    check = 0
    # gets length of the primes list
    size = len(primes)
    # for i = 0 min, size(primes) max
    for i in range(0, size):
        # if primes[i] > the sqare root of number - 1 break
        if (primes[i] > math.sqrt(number - 1)):
            break
        # if the number is divisible by the prime number at that index break
        if ((number - 1) % primes[i] == 0):
            check = 1
            break
        else:
            pass
    
    # if the number wasn't divisible by anything
    if (check == 0):
        primes.append(number - 1)
        counter += 1
        if (counter == number_of_primes):
            break
    else:
        check = 0
    # if we have all the primes we need
    if (number + 1) > biggest_prime:
        break

    # does the same thing as defore but with number + 1
    for i in range(0, size):
        if primes[i] > math.sqrt(number + 1):
            break
        if (number + 1) % (primes[i]) == 0:
            check = 1
            break
        else:
            pass
        
    if (check == 0):
        primes.append(number + 1)
        counter += 1
        if (counter == number_of_primes):
            break
    else:
        check = 0

print("\n")
sum = 0
for i in range(0, len(primes)):
    sum += primes[i]
print(sum)
