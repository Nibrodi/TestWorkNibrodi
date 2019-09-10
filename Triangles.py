import sys
i = 0
answer = []
n = int(input("Enter count: "))
while i < n:
    num = list(map(int, input("Enter numbers: ").split()))
    if num[0] + num [1] >= num[2] and num[1] + num[2] >= num[0] and num[0] + num[2] >= num[1]:
        answer.append(1)
    else:
        answer.append(0)
    i += 1
print(*answer)