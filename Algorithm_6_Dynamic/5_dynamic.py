# 금광
# 점화식
# 데이터 테이블의 i,j번째 원소 = 주어진 배열의 i,j번째 원소 + 데이터 테이블의 i-1,j-1 --의 i,j-1, --의 i+1,j-1번째 원소중 가장 큰값
# 데이터테이블의 1열은 주어진 배열의 1열과 같다
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n,m = map(int, sys.stdin.readline().split(' '))
    arr = list(map(int, sys.stdin.readline().split(' ')))
    dp = list()
    index = 0
    for h in range(n):
        dp.append(arr[index:index+m])
        index+=m
    print(dp)
# 찾으려는 배열의 원소에 대하여 왼쪽위, 왼쪽, 왼쪽 아래에서 오는 값들을 비교하여 최댓값을 찾는다.
    for j in range(1,m):
        # j = 열
        for v in range(n):
            # v = 행
            # 왼쪽 위에서 오는 경우
            if v == 0:
                left_up = 0
            else:
                left_up = dp[v-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if v == n-1:
                left_down = 0
            else:
                left_down = dp[v+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[v][j-1]
            dp[v][j] = dp[v][j] + max(left_up,left_down, left)

    answer = 0

    for k in range(n):
        answer = max(answer, dp[k][m-1])
    print(answer)



# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2