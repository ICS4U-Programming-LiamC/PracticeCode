# actually more efficient than anticipated
# got the sqrt idea from someone else
import math
num_divisors = 0
testNum = 0
num = 0
while (True):
    num_divisors = 0
    testNum += 1
    num = num + testNum
    for i in range(2, int(math.sqrt(num))):
        if(num % 60 != 0):
            break
        if(num % i == 0):
            num_divisors += 2
        else:
            pass
    if(num_divisors > 498):
        break
    else:
        # print(num_divisors)
        if (num_divisors > 50):
            print(num, num_divisors)

print(num, testNum, num_divisors)
