#1758 알바생 강호
N = int(input())
tipList = []
resultList = []

for _ in range(N):
    money = int(input())
    tipList.append(money)

tipList = sorted(tipList, reverse = True)

for i in range(N):
    result = tipList[i] - i
    if result < 0:
        break
    resultList.append(result)

print(sum(resultList))