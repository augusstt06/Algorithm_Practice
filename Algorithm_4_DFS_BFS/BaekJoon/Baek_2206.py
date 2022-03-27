# 백준 2206번 : 벽 부수기
from collections import deque
import sys

n, m  = list(map(int, sys.stdin.readline().split()))

arr = list()
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip())))

que = deque()
que.append([0, 0, 1])
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
visited[0][0][1] = 1
# [뚫은거, 안뚫은거]
def sol(que):
    while que:
        y,x,k = que.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x][k]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:

                if arr[ny][nx] == 0 and k == 1 and visited[ny][nx][k] == 0:
                    visited[ny][nx][k] = visited[y][x][k] + 1
                    que.append([ny, nx, k])

                if arr[ny][nx] == 1 and k == 1:
                    visited[ny][nx][0] = visited[y][x][1] + 1
                    que.append([ny, nx, 0])

                if arr[ny][nx] == 0  and k == 0 and visited[ny][nx][k] == 0:
                    visited[ny][nx][k] = visited[y][x][k] + 1
                    que.append([ny, nx, k])
    return -1
print(sol(que))

# if max(visited[n-1][m-1]) != 0:
#     print(max(visited[n-1][m-1])+1)
# else:
#     print(-1)

# 3 6
# 011100
# 010111
# 110010
