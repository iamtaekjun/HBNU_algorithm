# #1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)      


# #2
# N, M = map(int, input().split())
# listOfA = list(map(int, input().split()))
# listOfB = list(map(int, input().split()))

# resultList = listOfA + listOfB
# resultList = quick_sort(resultList)
# print(resultList)


# #3
# arrayList = [16, 8, 7, 3, 4, 3, 4, 1]
# pivot = (len(arrayList) // 2)
# left = 1
# right = 2
# flag = False

# for i in range(pivot):
#     if right == len(arrayList):
#         if arrayList[i] < arrayList[left]:
#             flag = False
#             break
#         else:
#             flag = True
#             break

#     if arrayList[i] < arrayList[left] and arrayList[i] < arrayList[right]:
#         flag = False
#         break
#     else:
#         flag = True
#         left += 2
#         right += 2

# if flag:
#     print("Right !")
# else:
#     print("Wrong !")


# #4
# def max_heapify(A, i):
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if(left < len(A) and A[left] > A[i]):
#         largest = left
#     else:
#         largest = i
    
#     if (right < len(A) and A[right] > A[largest]):
#         largest = right
    
#     if (largest != i):
#         A[i], A[largest] = A[largest], A[i]
#         max_heapify(A, largest)

# A = [4, 16, 15, 8, 7, 13, 14, 2, 5]
# n = (len(A) // 2) - 1

# for i in range(n-1, -1, -1):
#     max_heapify(A, i)

# print(A)


# #5
# import heapq as hq

# n = int(input())
# m = [int(n) for _ in range(n)]

# hq.heapify(m)
 
# if n == 1:
#     print(0)
# else:
#     answer = 0

#     while len(m) > 1:
#         a = hq.heappop(m)
#         b = hq.heappop(m)

#         hq.heappush(m, a+b)

#         answer += a+b

#     print(answer)