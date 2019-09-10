import sys
n = input("Enter count of numbers: ")
counts = input("Enter numbers: ").split()
sum = 0
for numbers in counts:
    sum += int(numbers)
print(sum)