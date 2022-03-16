# 영상 예제
# 음료수 얼려먹기
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
#
# def sol(a, b):
#     if a <= -1 or a >= n or b <= -1 or b >= m:
#         return False
#     if graph[a][b] == 0:
#         graph[a][b] = 1
#         print(a,b, 'a.b')
#         sol(a - 1, b)
#         sol(a, b - 1)
#         sol(a + 1, b)
#         sol(a, b + 1)
#         return True
#
#     return False
#
#
# answer = 0
#
# for j in range(n):
#     for h in range(m):
#         if sol(j, h):
#             answer += 1
# print(answer)

# 4 5
# 00110
# 00011
# 11111
# 00000

# 영상 예제 미로 탈출

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
from collections import deque

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def sol(a, b):
    que = deque()
    que.append((a, b))

    while que:
        a, b = que.popleft()
        for j in range(4):
            nx = dx[j] + a
            ny = dy[j] + b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[a][b] + 1
                que.append((nx, ny))
    return arr[n - 1][m - 1]


print(sol(0, 0))
