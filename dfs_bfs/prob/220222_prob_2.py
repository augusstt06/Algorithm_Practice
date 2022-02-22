# 문제 1
# 첫번째 줄에 얼음 틀의 세로길이 N과 가로길이 M이 주어집니다. (1 <= N, M <= 1000)
# 두번째 줄부터 N+1 번째 줄까지ㅣ 얼음 틀의 형태가 주어집니다
# 이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1입니다.
# 한번에 만들 수 있는 아이스크림의 갯수를 출력

# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 예시
# 3


# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j):
#             result += 1
# print(result)


# 문제 2
# n * m 크기의 미로
# 시작점의 위치는 (1,1), 출구는 (n,m)에 위치하며 한번에 한칸씩 이동할 수 있다.
# 통로가 있는곳을 1로, 없는 곳은 0 으로 표시된다.
# 탈출하기 위해 필요한 최소 칸의 갯수 (시작칸과 마지막 칸 포함하여 계산)

vol = input('입력').split()
n,m = map(int, vol)
print(n,m)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))