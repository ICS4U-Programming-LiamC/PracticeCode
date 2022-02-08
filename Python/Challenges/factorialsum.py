def factorial(num):
    total = 1
    for x in range(1, num+1):
        total = total * x
    return total

def sum(num):
    sum = 0
    string = str(num)
    for i in string:
        sum += int(i)
    return(sum)

def main():
    product = factorial(100)
    answer = sum(product)
    print(answer)

if __name__ == "__main__":
    main()
