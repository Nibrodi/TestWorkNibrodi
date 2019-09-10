import math
import sys
numbers = []
answer = []
i = 0
n = int(input("Enter count: "))
while i < n:
    numbers.append(list(map(int, input("Enter coordinats: ").split())))
    i += 1
#print(numbers)
for num in numbers:
    a = (num[1] - num[3]) / (num[0] - num[2])
    b = num[3] - a * num[2]
    answer.append('(%s %s)' % (str(int(a)), str(int(b))))
print(*answer)
#k = (y1 - y2) / (x1 - x2)
#b = y2 - k * x2
