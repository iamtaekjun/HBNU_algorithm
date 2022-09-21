# #1
# result = list(map(int, input().split()))
# result = sorted(result, reverse = True)
# print(result)
# print(max(result), result.index(max(result)))


# #2
# score = int(input())

# if score >= 90:
#     print('A')
# elif score >= 80 and score < 90:
#     print('B')
# elif score >= 70 and score < 80:
#     print('C')
# else:
#     print('기타')


# #3
# import random
# randList = []

# for _ in range(50):
#     randList.append(random.randint(0, 100))
# print(randList)

# setList = list(set(randList))
# print(setList)

# if randList != setList:
#     print('O')
# else:
#     print('X')


# #4
# number = int(input())

# for i in range(2, number):
#     if number % i == 0:
#         print("Not Prime Number")
#         exit()
# print("Prime Number")


# #5
# for i in range(6):
#     print(' ' * (5-i) + '*' * (i * 2 + 1))
# for i in range(6):
#     print(' ' * i + '*' * (11 - (2 * i)))


# #6
# string = input()
# count = 1
# resultString = ""

# for i in range(1, len(string)):
#     if (string[i - 1] == string[i]):
#         count += 1
#         continue
#     else:
#         resultString += string[i - 1] + str(count)
#         count = 1
# if string[-2] != string[-1]:
#     resultString += string[-1] + "1"
# else:
#     resultString += string[-1] + str(count)

# print(resultString)


# #7
# while True:
#     checkBox = [False, False, False, False]
#     passwd = input()
#     for i in range(len(passwd)):
#         if checkBox[0] == False:
#             if 33 <= ord(passwd[i]) <= 47 or 58 <= ord(passwd[i]) <= 64 or \
#              91 <= ord(passwd[i]) <= 96 or 123 <= ord(passwd[i]) <= 126:
#                 checkBox[0] = True

#         if checkBox[1] == False:
#             if 48 <= ord(passwd[i]) <= 57:
#                 checkBox[1] = True
#       
#         if checkBox[2] == False:
#             if 65 <= ord(passwd[i]) <= 90:
#                 checkBox[2] = True
        
#         if checkBox[3] == False:
#             if 97 <= ord(passwd[i]) <= 122:
#                 checkBox[3] = True

#     if checkBox[0] == True and checkBox[1] == True and checkBox[2] == True and checkBox[3] == True:
#         break
        

# for i in range(len(passwd)):
#     if 65 <= ord(passwd[i]) <= 90 :
#         passwd = passwd[:i] + (chr(ord(passwd[i])+32)) + passwd[i+1:]

# print(passwd)


# #8
# n, k  = map(int, input().split())

# numberList = list(map(int, input().split()))
# numberList.sort(reverse=True)
# sum = []
# for i in range(len(numberList)-2):
# 	for j in range(len(numberList)-1):
# 		for k in range(len(numberList)):
# 			sum.append(numberList[i] + numberList[j] + numberList[k])
			
# setList = list(set(sum))
# setList.sort(reverse=True)

# print(setList[k])