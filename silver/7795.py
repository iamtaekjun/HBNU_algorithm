#7795 먹을 것인가 먹힐 것인가  (이분 탐색)
testCase = int(input())
for _ in range(testCase):
    A, B = map(int, input().split())

    predator = list(map(int, input().split()))
    prey = list(map(int, input().split()))

    predator.sort()
    prey.sort()









































    # count = 0
    # # for i in range(len(predator)-1, -1, -1):
    # #     for j in range(len(prey)-1, -1, -1):
    # #         if predator[i] <= prey[0]:
    # #             print(count)
                

    # #         if predator[i] > prey[j]:
    # #             count += j + 1
    # #             break
    # predatorIndex = len(predator) - 1
    # preyIndex = len(prey) - 1

    # while True:
    #     if predator[predatorIndex] <= prey[0]:
    #         break

    #     if predator[predatorIndex] > prey[preyIndex]:
    #         count += (preyIndex + 1)
    #         predatorIndex -= 1
    #         preyIndex = len(prey)

    #         if predatorIndex < 0:
    #             break

    #     preyIndex -= 1

    # print(count)
            

    