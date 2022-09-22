#2839
weightOfSugar = int(input())
numberOfBags = 0

while True:
    if weightOfSugar % 5 == 0:
        print(numberOfBags + (weightOfSugar // 5))
        break
    
    weightOfSugar -= 3
    numberOfBags += 1

    if weightOfSugar == 0:  
        print(numberOfBags)
        break
    elif weightOfSugar < 0:
        print(-1)
        break