# 백준 7569번 :  토마토 3차원
from collections import deque

n, m, h = map(int, input().split())

arr = list()

for _ in range(h):
    temp = list()
    for _ in range(m):
        temp.append(list(map(int, input().split())))
    arr.append(temp)


dz = [0, 0, -1, 1, 0 ,0]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

visited = list()
for _ in range(h):
    temp = list()
    for z in range(m):
        temp.append([0] * n)
    visited.append(temp)

answer = 0
index_list = list()
possible = True
que = deque()

# 000 024
def sol(que):
    global answer
    while que:
        for _ in range(len(que)):
            z, y, x = que.popleft()
            visited[z][y][x] = 1
            for j in range(6):
                nz = z + dz[j]
                ny = y + dy[j]
                nx = x + dx[j]
                if h > nz >= 0 and m > ny >= 0 and n > nx >= 0 and visited[nz][ny][nx] == 0 and arr[nz][ny][nx] == 0:
                    que.append([nz, ny, nx])
                    visited[nz][ny][nx] = 1
        answer += 1
    return answer


for t in range(h):
    for s in range(m):
        for q in range(n):
            if arr[t][s][q] == 1:
                que.append([t,s,q])
sol(que)

for u in range(h):
    for f in range(m):
        for v in range(n):
            if arr[u][f][v] == -1:
                visited[u][f][v] = 1
            if visited[u][f][v] == 0:
                possible = False
                break
if possible:
    print(answer - 1)
else:
    print(-1)

