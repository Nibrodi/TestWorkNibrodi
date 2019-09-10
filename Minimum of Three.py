import sys

i = 1
twins = []
n = input("Enter count of twins: ")
while i <= int(n):
    twins.append(input("Enter numbers: ").split())
    i += 1
for numbers in twins:
    if int(numbers[0]) < int(numbers[1]) < int(numbers[2]):
        print(int(numbers[0]))
    elif int(numbers[1]) < int(numbers[2]):
        print(int(numbers[1]))
    else:
        print(int(numbers[2]))