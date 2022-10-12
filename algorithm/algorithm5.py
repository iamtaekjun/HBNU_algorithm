# #1
# def mergeSort(arr):
#     if len(arr) == 1:
#         return arr
    
#     mid = len(arr) // 2

#     st_arr = mergeSort(arr[:mid])
#     end_arr = mergeSort(arr[mid:])

#     result = []
#     st = end = 0

#     while st < len(st_arr) and end < len(end_arr):
#         if st_arr[st] < end_arr[end]:
#             result.append(st_arr[st])
#             st += 1
#         else:
#             result.append(end_arr[end])
#             end += 1

#     result += st_arr[st:]
#     result += end_arr[end:]
    
#     return result

# #2
# def mergeSortReverse(arr):
#     if len(arr) == 1:
#         return arr
    
#     mid = len(arr) // 2

#     st_arr = mergeSortReverse(arr[:mid])
#     end_arr = mergeSortReverse(arr[mid:])

#     result = []
#     st = end = 0

#     while st < len(st_arr) and end < len(end_arr):
#         if st_arr[st] > end_arr[end]:
#             result.append(st_arr[st])
#             st += 1
#         else:
#             result.append(end_arr[end])
#             end += 1

#     result += st_arr[st:]
#     result += end_arr[end:]
    
#     return result


# #3
# array = list(map(int, input().split()))
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# resultArray = []

# for i in range(len(commands)):
#     start = commands[i][0]
#     end = commands[i][1]

#     sortArray = []
#     for j in range(start-1, end):
#         sortArray.append(array[j])

#     sortArray = mergeSort(sortArray)             

#     resultArray.append(sortArray[commands[i][2] - 1])

# print(resultArray)


# #4 - 1 
# numberList = list(map(str, input().split()))
# strList = [(i*3) for i in numberList]
# result = ""

# strList = mergeSortReverse(strList)
# strList = [i[:len(i)//3] for i in strList]

# for i in strList:
#     result += i

# print(result)


# #4 - 2
# from itertools import permutations

# numbers = input().split(" ")
# new_numbers = []

# for i in permutations(numbers, len(numbers)):
#     string = ""

#     for j in i:
#         string += j

#     new_numbers.append(string)

# new_numbers = list(map(int, new_numbers))
# new_numbers = mergeSortReverse(new_numbers)

# print(new_numbers[0])
