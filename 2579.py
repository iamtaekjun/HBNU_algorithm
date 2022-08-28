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