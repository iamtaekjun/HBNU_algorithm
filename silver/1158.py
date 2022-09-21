#1158 요세푸스 순열(원형 큐)
josephusPermutation = []
circularQueue = []

N, K = map(int, input().split())

for i in range(1, N + 1):
    circularQueue.append(i)    #ex) N = 3, cQ = [1, 2, 3]

indexNumber = 0

for _ in range(N):        #N번 요세푸스 순열에 pop되는 값을 대입
    indexNumber = (indexNumber + K-1) % len(circularQueue)  #원형 큐 식 : 인덱스 = (현재 인덱스 + 증가값?) % 큐의 길이(Size)
    josephusPermutation.append(circularQueue.pop(indexNumber))  #append

print("<", end = ""), print(*josephusPermutation, sep = ', ', end = ">") #출력