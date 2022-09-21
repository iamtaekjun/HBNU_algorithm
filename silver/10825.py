#10825 국영수 (정렬)
N = int(input())
studentInfo = []

for _ in range(N):
    name, korean, english, math = map(str, input().split())
    studentInfo.append([name, int(korean), int(english), int(math)])

studentInfo = sorted(studentInfo, key = lambda x : x[0])
studentInfo = sorted(studentInfo, key = lambda x : x[3], reverse = True)
studentInfo = sorted(studentInfo, key = lambda x : x[2])
studentInfo = sorted(studentInfo, key = lambda x : x[1], reverse = True)

for i in range(N):
    print(studentInfo[i][0])