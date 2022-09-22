# #1931 회의실 배정 (정렬, 그리디) 시간초과
# N = int(input())
# startEndList = []
# countList = []

# for _ in range(N):
#     start, end = map(int, input().split())
#     startEndList.append([start, end])


# startEndList = sorted(startEndList, key = lambda x : x[1])
# startEndList = sorted(startEndList, key = lambda x : x[0])


# for i in range(N):
#     endTime = startEndList[i][1]   #6
#     count = 1

#     for j in range(i+1, N):
#         if startEndList[j][0] >= endTime:
#             endTime = startEndList[j][1]
#             count += 1
    
#     countList.append(count)

# print(max(countList))


#1931 회의실 배정(정렬, 그리디) 성공
N = int(input())
resultList = []

for i in range(N):
    start, end = map(int, input().split())
    resultList.append([start, end])

resultList.sort()

clear = 0
count = 0
for i in range(N):
    if resultList[i][0] < clear:         #resultList[i][0] == start      /      resultList[i][1] == end
        continue
    
    j = i + 1
    if j == N:
        count += 1
        break

    flag = False
    while resultList[i][1] > resultList[j][0]:
        if resultList[i][1] > resultList[j][0] and resultList[i][1] > resultList[j][1]:
            flag = True
            break
        
        j += 1

        if j == N:
            break
    
    if flag == False:
        clear = resultList[i][1]
        count += 1

print(count)

    