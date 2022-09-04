#1026 보물(그리디 알고리즘)
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

for _ in range(N):
    minIndexNumberOfAAAA = A.index(min(A))
    maxIndexNumberOfBBBB = B.index(max(B))
    S += A[minIndexNumberOfAAAA] * B[maxIndexNumberOfBBBB]

    A.pop(minIndexNumberOfAAAA), B.pop(maxIndexNumberOfBBBB)

print(S)