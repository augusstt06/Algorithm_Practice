# dfs     : 깊이 우선 탐색 ==> 스택 자료구조(재귀함수)를 이용한다
# 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입, 방문 처리 (문제에 따라 인접 노드 방문 기준 정하기)
# 2. 스택의 최상단 노드에 방문 하지 않은 인접 노드가 1개라도 있다면 해당 노드를 스택에 넣고 방문 처리, 인접 노드가 없다면 스택에서 최상단 노드 꺼냄
# 3. 2번 과정이 더이상 실행되지 않을때까지 반복
graph = [
    # 각 노드가 연결된 정보를 리스트로 표현
    [],
    # 1번 노드 연결
    [2, 3, 8],
    # 2번 노드 연결
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 노드가 방문한 정보를 표현 아직 방문 전이기 때문에 모두 False로 표현
visited = [False] * 9

# print(visited)
# 메서드 정의

def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    # print(visited)
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문한다
    for i in graph[v]:
        # print(graph[v], '범위')
        # print(i, '최초i')
        # print(visited[i], '확인ㄴ')

        # 만약 visited[i]가 False면 ==> 방문 하지 않았다면
        if not visited[i]:
            # print(i, 'if절')
            dfs(graph, i, visited)


dfs(graph,1, visited)