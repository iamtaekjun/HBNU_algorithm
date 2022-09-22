#2606
numberOfComputer = int(input())
edges = int(input())

graph = [[] for _ in range(numberOfComputer + 1)]

for i in range(edges):
    first, end = map(int, input().split())
    graph[first].append(end)
    graph[end].append(first)

def findGraph(vertex, visited = []):
    visited.append(vertex)

    for i in graph[vertex]:
        if not i in visited:
            visited = findGraph(i, visited)

    return visited

visitedGraphList = findGraph(1)   #1

print(len(visitedGraphList) - 1)