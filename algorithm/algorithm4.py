#1
def selection_Sort(array):      #선택

    n = len(array)
    for i in range(n-1):
        minIdx = i
        for k in range(i + 1, n):
            if (array[minIdx] > array[k]):         #최솟값을 찾음
                minIdx = k
        array[i], array[minIdx] = array[minIdx], array[i]

    return array

def insertion_Sort(array):     #삽입
    n = len(array)
    for end in range(n):
        for cur in range(end, 0, -1):
            if(array[cur - 1] > array[cur]):
                array[cur - 1], array[cur] = array[cur], array[cur - 1]
    return array

def bubble_sort(array):      #버블
    n = len(array)
    for i, end in enumerate(range(n - 1, 0, -1)):     #0 9 / 1 8 ...
        is_change = False

        for curr in range(0, end):
            if array[curr] > array[curr + 1]:
                array[curr], array[curr + 1] = array[curr + 1], array[curr]
                is_change = True 

        if not is_change:
            break
    return array


# #2
# def selection_Sort_Reverse(array):      

#     n = len(array)
#     for i in range(n-1):
#         maxIdx = i
#         for k in range(i + 1, n):
#             if (array[maxIdx] < array[k]):         
#                 maxIdx = k
#         array[i], array[maxIdx] = array[maxIdx], array[i]

#     return array

# N, k = map(int, input().split())

# numberList = list(map(int, input().split()))

# selection_Sort_Reverse(numberList)

# print(numberList[k - 1])


# #3
# N = int(input())
# zoapyoList = []

# for _ in range(N):
#     a, b = map(int, input().split())
#     zoapyoList.append([a, b])

# def selection_Sort_2dimension(array):      #선택

#     n = len(array)
#     for i in range(n-1):
#         minIdx = i
#         for k in range(i + 1, n):
#             if (array[minIdx][1] > array[k][1]):
#                 minIdx = k
#         array[i], array[minIdx] = array[minIdx], array[i]

#     return array

# selection_Sort_2dimension(zoapyoList)

# for i in range(len(zoapyoList)):
#     print(*zoapyoList[i])


# #4
# N = int(input())
# intInCardList = list(map(int, input().split()))
# M = int(input())
# howManyCardList = list(map(int, input().split()))

# resultList = []
# # selectionSort(intInCardList)

# # for i in range(len(howManyCardList)):
# #     if intInCardList[i] in howManyCardList:
# #         for j in range(intInCardList.index(howManyCardList[i]), )

# for i in range(len(howManyCardList)):
#     resultList.append(intInCardList.count(howManyCardList[i]))

# print(resultList)


# #5
# N = int(input())
# zoapyoList = list(map(int, input().split()))
# countSmall = [0*i for i in range(N)]
# overlapCheckDic = {}

# indexCount = 0
# for x in range(N):
#     for i in range(N):
#         if zoapyoList[x] > zoapyoList[i]:
#             if zoapyoList[i] in overlapCheckDic:
#                 continue

#             overlapCheckDic[zoapyoList[i]] = True
#             countSmall[indexCount] += 1
    
#     overlapCheckDic = {}
#     indexCount += 1

# print(*countSmall)


