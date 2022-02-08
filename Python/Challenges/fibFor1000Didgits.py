import math
small = 1
big = 1
counter = 0
index = 2
while(counter < 10): # math.log(x, 10) < 1000
    new = small + big
    small = big
    big = new
    index += 1
    if len(str(big)) >= 999:
        print(index, len(str(big)))
        counter += 1
# print(x, counter)
# print(len(str(x)))
