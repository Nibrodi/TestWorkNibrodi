import sys

i = 1
twins = []
n = input("Enter count of twins: ")
while i <= int(n):
    twins.append(list(map(int, input("Enter numbers: ").split())))
    i += 1
for numbers in twins:
    if numbers[0] < numbers[1] and numbers[0] < numbers[2]:
        print(numbers[0])
    elif numbers[1] < numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])













