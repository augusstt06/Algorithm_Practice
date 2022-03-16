# 백준 2606
from collections import deque

n = int(input())
m = int(input())
arr = list()
for _ in range(m):
    arr.append(list(map(int, input().split())))

visited = [False] * n
node = list()

for i in range(n + 1):
    route = list()
    for j in arr:
        if i == j[0]:
            route.append(j[1])
        elif i == j[1]:
            route.append(j[0])
    route.sort()
    node.append(route)


def bfs(node, start, visited):
    count = 0
    que = deque()
    que.append(start)
    visited[start - 1] = True
    while que:
        v = que.popleft()
        for s in node[v]:
            if not visited[s - 1]:
                visited[s - 1] = True
                count += 1
                que.append(s)
    return print(count)
bfs(node, 1, visited)

