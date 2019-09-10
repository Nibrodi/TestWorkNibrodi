import sys
import math
far = ''
i = 1
num = list(map(int, input("Enter numbers: ").split()))
n = num[0]
while i <= n:
    x = (num[i] - 32) / 1.8
    far += (str(round(x)) + ' ')
    i += 1
print(far)
