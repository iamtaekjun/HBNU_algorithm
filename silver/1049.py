#1049 기타줄
listOfBrand = []       #각 브랜드의 패키지가격, 낱개 가격 입력
listToCompare = []     #비교하기 위한 리스트
flag = False

numberOfLine, M = map(int, input().split())

for _ in range(M):
    package, piece = map(int, input().split())
    listOfBrand.append([package, piece])

cost = 0            #최종 cost

while numberOfLine > 6:          #끊어진 줄의 개수가 6 이상일 때,
    if flag == False:            #플래그 조건을 달아 한번만 사용하기 위함
        for i in range(M):
            listToCompare.append(listOfBrand[i][0])
            listToCompare.append(listOfBrand[i][1] * 6)
    
    cost += min(listToCompare)     #가장 작은거 cost에 더해주기
    numberOfLine -= 6           #끊어진 줄의 개수 빼주는 것 잊지 말기 !

    flag = True             

listToCompare.clear()           #비교하기 위한 list clear

for i in range(M):               #끊어진 줄의 개수가 6 미만일 때,
    listToCompare.append(listOfBrand[i][0])
    listToCompare.append(listOfBrand[i][1] * numberOfLine)   

cost += min(listToCompare)

print(cost)