import sys
i = 1
twins = []
n = input("Enter count of twins: ")
while i <= int(n):
    twins.append(input("Enter numbers: ").split())
    i += 1
for numbers in twins:
    print(int(numbers[0]) + int(numbers[1]))
