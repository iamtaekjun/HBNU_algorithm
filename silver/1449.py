#1449 수리공 항승
numberOfTape, lengthOfTape = map(int, input().split())
leakList = list(map(int, input().split()))

leakList.sort()

start = leakList[0]
end = leakList[0] + lengthOfTape
count = 1

for i in range(numberOfTape):
    if start <= leakList[i] < end:
        continue
    else:
        start = leakList[i]
        end = leakList[i] + lengthOfTape

        count += 1
    
print(count)
