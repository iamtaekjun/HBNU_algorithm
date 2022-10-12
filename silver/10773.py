#10773 제로 (스택)
K = int(input())
numberList = []

top = -1
for _ in range(K):
    a = int(input())

    if a == 0:
        numberList.pop(top)
        top -= 1
    else:
        numberList.append(a)
        top += 1

print(sum(numberList))