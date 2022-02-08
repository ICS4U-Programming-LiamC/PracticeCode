def gridCounter(size):
    row = []
    grid = []
    for i in range(0, size + 1):
        row.append(1)

    size += 1
    for x in range(0, size):
        previousRow = row
        grid.append(row)
        row = []
        previous = 0
        for i in range(0, size):
            row.append(previousRow[i] + previous)
            previous = previousRow[i] + previous

    for i in grid:
        print(i)
    




def main():
    gridCounter(6)

main()