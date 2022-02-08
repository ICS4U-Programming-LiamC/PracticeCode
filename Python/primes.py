###################################### EXPLANATION / LOGIC ######################################

# program that finds all prime numbers between 2, and "biggest_prime"
# checks numbers that are a multiple of 6+-1. This works because any prime number + or - 1 is even
# and therefor divisible by 2
# one of those two numbers will also be divisible by three since there is a multiple of three every three numbers
# and we know the prime number isn't one, so one of the two next to it must be
# if a number is divisible by both 2 and 3 it is a multiple of 6
# therefore any prime number must sit next to a multiple of 6

# this program divides the supposed prime by all prime numbers before it. We can do this because
# all numbers can be written as the product of other primes
# example 54 = 2 * 3 * 3 * 3
# we can also save time by only checking prime numbers that are less than the sqareroot of the supposed prime numbers
# since we are checking if two numbers multiply to make it we are able to only check the bottom half of those numbers
# example: factors of 12: 1, 12 | 2, 6 | 3, 4
# you only have to check 1, 2, 3 because they correspond to the other factor of their set
# if 2 doesn't work neither will 6

######################################## ACTUAL CODE ###############################################

# imports an unecessary math function, could use 2//var instead of math.sqrt(var)
import math

# initializes global vars, 2 and 3 are seed numbers to get the program started
biggest_prime = 1000000
primes = [2, 3]

# for each number between 6, and the specified biggest prime, step by 6
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
    else:
        check = 0

# prints the list of primes, and how many total primes there were
# When using big biggest_prime make sure to disable the print function
print("\n")
print(primes)
print("There are", len(primes), "total primes in your interval")
