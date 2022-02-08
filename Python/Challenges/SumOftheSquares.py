sumSquare = 0
squareSum = 0
sum = 0
for each in range(1, 101):
    sumSquare += each**2
    sum += each
    print(each)

squareSum = sum ** 2
answer = squareSum - sumSquare
print(sum)
print(squareSum)
print(sumSquare)
print(answer)
