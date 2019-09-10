import math
import sys
i = 0
answer = []
def arith(a, b, n):
    i = 0
    y = 0
    while i < n:
        x = a + b * i
        y += x
        i += 1
    return y
n = int(input("Enter count: "))
while i < n:
    num = list(map(int, input("Enter numbers: ").split()))
    answer.append(arith(a = num[0], b = num[1], n = num[2]))
    i += 1
print(*answer)