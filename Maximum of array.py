import sys
nums = input("Enter numbers: ").split()
min = 0
max = 0
#print(nums)
for number in nums:
    if min < int(number):
        min = int(number)
        continue
    if max > int(number):
        max = int(number)
print('answer:' + str(min) + ' ' + str(max))