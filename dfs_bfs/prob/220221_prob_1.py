# 백준 dfs문제
# 첫째줄에 정점의 갯수 N (1 <= N <= 1000), 간선의 갯수 M (1 <= N <= 10000)
# 탐색을 시작할 정점의 번호 V가 주어진다.
# M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. (두 정점 사이 여러개의 간선이 있을수 있다.)
# 탐색결과를 리턴해라
# 4 5 1 ==> n = 4(정점의 갯수), m = 5(간선의 갯수), v = 1(탐색 시작 번호)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 예제 입력1
visited = [False] * 5
vertex_graph = [
    [4, 5, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [3, 4]
]

# 예제 입력2
# visited = [False] * 6
# vertex_graph = [
#     [5,5,3],
#     [5,4],
#     [5,2],
#     [1,2],
#     [3,4],
#     [3,1]
# ]


# 예제 입력3
# visited = [False] * 1001
# vertex_graph = [
#     [1000, 1, 1000],
#     [999, 1000]
# ]
#
# n = vertex_graph[0][0]
# m = vertex_graph[0][1]
# v = vertex_graph[0][2]

connect_route = []
for i in range(n+1):
    route = []
    for j in vertex_graph[1::]:
        if i == j[0]:
            route.append(j[1])
        elif i ==j[1]:
            route.append(j[0])
    connect_route.append(sorted(route))


def dfs(connect_route, v, visited):
    visited[v] = True
    print(v, end=' ')
    for h in connect_route[v]:
        if not visited[h]:
            dfs(connect_route, h, visited)


dfs(connect_route, v, visited)


