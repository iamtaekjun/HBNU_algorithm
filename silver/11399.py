#11399 ATM(정렬)
N = int(input())
accountList = list(map(int, input().split()))

accountList.sort()
sum = 0
tmp = 0

for i in range(N):
    sum += tmp + accountList[i]  

    tmp += accountList[i]  

print(sum)  