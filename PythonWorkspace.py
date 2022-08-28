# #2839
# weightOfSugar = int(input())
# numberOfBags = 0

# while True:
#     if weightOfSugar % 5 == 0:
#         print(numberOfBags + (weightOfSugar // 5))
#         break
    
#     weightOfSugar -= 3
#     numberOfBags += 1

#     if weightOfSugar == 0:  
#         print(numberOfBags)
#         break
#     elif weightOfSugar < 0:
#         print(-1)
#         break


# #2606
# numberOfComputer = int(input())
# edges = int(input())

# graph = [[] for _ in range(numberOfComputer + 1)]

# for i in range(edges):
#     first, end = map(int, input().split())
#     graph[first].append(end)
#     graph[end].append(first)

# def findGraph(vertex, visited = []):
#     visited.append(vertex)

#     for i in graph[vertex]:
#         if not i in visited:
#             visited = findGraph(i, visited)

#     return visited

# visitedGraphList = findGraph(1)   #1

# print(len(visitedGraphList) - 1)


# #1302
# numberOfBooksSold = int(input())
# nameOfBooks = []
# countOfBooks = []

# for _ in range(numberOfBooksSold):
#     nameOfBooks.append(input())

# bookSeted = list(set(nameOfBooks))
# bookSeted = sorted(bookSeted)

# for name in bookSeted:
#     countOfBooks.append(nameOfBooks.count(name))

# print(bookSeted[countOfBooks.index(max(countOfBooks))])  


# #1149 실패
# numberOfHouse = int(input())
# rgb = []
# finalCost = 0
# flag = False

# for _ in range(numberOfHouse):
#     rgb = list(map(int, input().split()))
#     if flag == True:
#         rgb[indexNumber] = 1001

#     minimumNumber = min(rgb)
#     finalCost += minimumNumber
#     indexNumber = rgb.index(minimumNumber)

#     flag = True
    
# print(finalCost)        #수정해야됨  마지막 예제 오류
# #현재 비용만 보고 고르게 되면 최종적으로 최솟값을 구하지 못할 수 있음
# #3개의 색을 다 칠했을 때 다음 비용을 따져봐야 할듯


# #1158 요세푸스 순열(원형 큐)
# josephusPermutation = []
# circularQueue = []

# N, K = map(int, input().split())

# for i in range(1, N + 1):
#     circularQueue.append(i)    #ex) N = 3, cQ = [1, 2, 3]

# indexNumber = 0

# for _ in range(N):        #N번 요세푸스 순열에 pop되는 값을 대입
#     indexNumber = (indexNumber + K-1) % len(circularQueue)  #원형 큐 식 : 인덱스 = (현재 인덱스 + 증가값?) % 큐의 길이(Size)
#     josephusPermutation.append(circularQueue.pop(indexNumber))  #append

# print("<", end = ""), print(*josephusPermutation, sep = ', ', end = ">") #출력


# #1991 트리 순회  (실패)
# class TreeNode():
#     def __init__(self):
#         self.left = None
#         self.data = None
#         self.right = None

# def firstTree(rootNode, firstLeft, firstRight):
#     node1 = TreeNode()
#     node1.data = rootNode

#     if firstLeft != '.':
#         node2 = TreeNode()
#         node2.data = firstLeft
#         node1.left = node2

#     if firstRight != '.':
#         node3 = TreeNode()
#         node3.data = firstRight
#         node1.right = node3
    
#     return node1

# def insertTree(thatNode, leftData, rightData, root):
#     current = root

#     while True:
#         if thatNode == str(current.data):    #찾음
#             if leftData != '.':
#                 node1 = TreeNode()
#                 node1.data = leftData
#                 current.left = node1                            #밑에 트리순회 도는 것처럼 찾으면 될듯? 재기 사용       runtime error 발생하면 첨부터 ㄱ
#             if rightData != '.':
#                 node2 = TreeNode()
#                 node2.data = rightData
#                 current.right = node2
#             break
#         elif thatNode < str(current.data):
#             if current.left == None:
#                 break
#             current = current.left
#         elif thatNode > str(current.data):
#             if current.right == None:
#                 break
#             current = current.right
    
#     return root

# def preorder(node):
#     if node == None:
#         return
#     print(node.data, end = "")
#     preorder(node.left)
#     preorder(node.right)

# def inorder(node):
#     if node == None:
#         return 
#     inorder(node.left)
#     print(node.data, end = "")
#     inorder(node.right)

# def postorder(node):
#     if node == None:
#         return 
#     postorder(node.left)
#     postorder(node.right)
#     print(node.data, end = "")

# #main
# N = int(input())
# rootNode, firstLeft, firstRight = map(str, input().split())
# flag = False

# root = firstTree(rootNode, firstLeft, firstRight)

# for _ in range(N - 1):       #입력
#     node, leftDescendent, rightDescendent = map(str, input().split())

#     if flag == False:
#         resultRoot = insertTree(node, leftDescendent, rightDescendent, root)

#     if flag == True:
#         resultRoot = insertTree(node, leftDescendent, rightDescendent, temp)

#     temp = resultRoot
#     flag = True

# preorder(temp), print()
# inorder(temp), print()
# postorder(temp), print()    #정렬트리가 아니기때문에 data의 크기로 비교를 하며 찾아가면 안됨


# #1026 보물(그리디 알고리즘) 수정필요
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# S = 0

# for _ in range(N):
#     minIndexNumberOfAAAA = A.index(min(A))
#     maxIndexNumberOfBBBB = B.index(max(B))
#     S += A[minIndexNumberOfAAAA] * B[maxIndexNumberOfBBBB]

#     A.pop(minIndexNumberOfAAAA), B.pop(maxIndexNumberOfBBBB)

# print(S)        #푼 방식이 문제의 의도와 다름  나중에 다시 풀 것


# #1049 기타줄
# listOfBrand = []       #각 브랜드의 패키지가격, 낱개 가격 입력
# listToCompare = []     #비교하기 위한 리스트
# flag = False

# numberOfLine, M = map(int, input().split())

# for _ in range(M):
#     package, piece = map(int, input().split())
#     listOfBrand.append([package, piece])

# cost = 0            #최종 cost

# while numberOfLine > 6:          #끊어진 줄의 개수가 6 이상일 때,
#     if flag == False:            #플래그 조건을 달아 한번만 사용하기 위함
#         for i in range(M):
#             listToCompare.append(listOfBrand[i][0])
#             listToCompare.append(listOfBrand[i][1] * 6)
    
#     cost += min(listToCompare)     #가장 작은거 cost에 더해주기
#     numberOfLine -= 6           #끊어진 줄의 개수 빼주는 것 잊지 말기 !

#     flag = True             

# listToCompare.clear()           #비교하기 위한 list clear

# for i in range(M):               #끊어진 줄의 개수가 6 미만일 때,
#     listToCompare.append(listOfBrand[i][0])
#     listToCompare.append(listOfBrand[i][1] * numberOfLine)   

# cost += min(listToCompare)

# print(cost)


# #14501 퇴사 (실패)  다시하기
# n = int(input())
# t = []
# p = []
# dp = []
# for i in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)
#     dp.append(b)
# dp.append(0)
# for i in range(n - 1, -1, -1):
#     if t[i] + i > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
# print(dp[0])



#2579 계단오르기
stair = int(input())          #계단 개수

weight = [0]                   #가중치

for _ in range(stair):        #가중치 리스트에 값 추가
    a = int(input())
    weight.append(a)

g = [0, 0]   #한칸 전에서 올라온 거
h = [0, weight[1]]           #두칸 전에서 올라온 거

for i in range(2, stair + 1):
    g.append(0)
    h.append(0)

    g[i] = h[i - 1] + weight[i]
    h[i] = max(g[i - 2], h[i - 2]) + weight[i]

print(max(g[-1], h[-1]))






