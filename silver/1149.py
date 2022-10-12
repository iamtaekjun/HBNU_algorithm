#1149 실패
numberOfHouse = int(input())
rgb = []
finalCost = 0
flag = False

for _ in range(numberOfHouse):
    rgb = list(map(int, input().split()))
    if flag == True:
        rgb[indexNumber] = 1001

    minimumNumber = min(rgb)
    finalCost += minimumNumber
    indexNumber = rgb.index(minimumNumber)

    flag = True
    
print(finalCost)        #수정해야됨  마지막 예제 오류
#현재 비용만 보고 고르게 되면 최종적으로 최솟값을 구하지 못할 수 있음
#3개의 색을 다 칠했을 때 다음 비용을 따져봐야 할듯