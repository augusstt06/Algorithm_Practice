from collections import deque

n, m, v = map(int, input().split())
arr = list()
for c in range(m):
    arr.append(list(map(int, input().split())))

visited_dfs = [False] * n
visited_bfs = [False] * n
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


def dfs(node, v, visited_dfs):
    visited_dfs[v - 1] = True
    print(v, end=' ')
    for h in node[v]:
        if not visited_dfs[h - 1]:
            dfs(node, h, visited_dfs)


def bfs(node, v, visited_bfs):
    que = deque()
    que.append(v)
    visited_bfs[v - 1] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for s in node[v]:
            if not visited_bfs[s - 1]:
                visited_bfs[s - 1] = True
                que.append(s)


dfs(node, v, visited_dfs)
print()
bfs(node, v, visited_bfs)
