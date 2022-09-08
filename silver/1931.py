#1931 회의실 배정 (정렬, 그리디)
N = int(input())
startEndList = []
countList = []

for _ in range(N):
    start, end = map(int, input().split())
    startEndList.append([start, end])


startEndList = sorted(startEndList, key = lambda x : x[1])
startEndList = sorted(startEndList, key = lambda x : x[0])


for i in range(N):
    endTime = startEndList[i][1]   #6
    count = 1

    for j in range(i+1, N):
        if startEndList[j][0] >= endTime:
            endTime = startEndList[j][1]
            count += 1
    
    countList.append(count)

print(max(countList))