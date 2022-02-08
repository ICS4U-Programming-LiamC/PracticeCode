answer = 0
for each in range(0, 1000):
    if (each % 3 == 0) or (each % 5 == 0):
        answer += each

print(answer)
