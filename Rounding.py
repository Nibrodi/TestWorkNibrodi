import sys
import math
i = 1
twins = []
n = input("Enter count of twins: ")
while i <= int(n):
    twins.append(input("Enter numbers: ").split())
    i += 1
for nums in twins:
    print(round(int(nums[0]) / int(nums[1])))