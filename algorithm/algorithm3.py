# #1
# def desc(n):
#     n = n[::-1]

#     return n

# n = input()
# print(desc(n))


# #2
# resultList = []
# def reverse(number):
#     reverseNumber = []
#     for i in range(len(number)):
#         temp = str(number[i])
#         temp = int(temp[::-1])
        
#         reverseNumber.append(temp)
    
#     return reverseNumber

# def isPrime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return resultList
#     resultList.append(number)

#     return resultList
               
# N = int(input())
# number = list(map(int, input().split()))

# reverseNumber = reverse(number)
# for i in range(len(reverseNumber)):
#     resultList = isPrime(reverseNumber[i])
    
# print(resultList)


# #3 - 1
# A, B, V = map(int, input().split())
# date = 0

# while True:
#     V -= A
#     if V <= 0:
#         date += 1
#         break
#     V += B
#     date += 1

# print(date)
# #3 - 2      Ax - B(x-1) = V     >>    x = (V-B) / (A-B)
# A, B, V = map(int, input().split())

# x = (V - B) / (A - B)
# if x == (int(x)):
#     print(int(x))
# else:
#     print(int(x+1))


# #4 
# N = int(input())

# score = list(map(int, input().split()))
# average = round((sum(score) / N))
# print(average)
# sortScore = sorted(score)
# temp = 1000000000000

# for i in range(len(sortScore)):
#     if abs(sortScore[i] - average) <= abs(temp):
#         temp = (sortScore[i] - average)
#         resultList = [average, score.index(sortScore[i]) + 1]

# print(resultList)



# #5
# N, M = map(int, input().split())
# numbers = list(map(int, input().split()))
# num_sum, count = 0, 0

# for i in range(0, N):
#     for j in range(i, N):
#         num_sum += numbers[j]
#         if num_sum == M:
#             count+=1
#             break

#     num_sum = 0

# print(count)



# #6
# flag = True
# matrix = []
# for i in range(4):           #change
#     numbers = list(map(int, input().split()))
#     matrix.append(numbers)

# root = int(len(numbers)**(1/2))

# for i in range(len(numbers)):
#     chk_row = [0] * (len(numbers)+1)
#     chk_col = [0] * (len(numbers)+1)

#     for j in range(len(numbers)):
#         if chk_row[matrix[i][j]]:
#             flag = False
#             break

#         chk_row[matrix[i][j]] = 1

#         if chk_col[matrix[j][i]]:
#             flag = False
#             break

#         chk_col[matrix[j][i]] = 1

#         if i % root == 0 and j % root == 0:
#             chk_block = [0] * (len(numbers)+1)

#             for row in range(i, i+root):
#                 for col in range(j, j+root):
#                     if chk_block[matrix[row][col]]:
#                         flag = False
#                         break

#                     chk_block[matrix[row][col]] = 1
# if flag:
#     print("YES")
# else: 
#     print("NO")