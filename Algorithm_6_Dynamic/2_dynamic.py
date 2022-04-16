# 1로 만들기
# 정수x가 5, 3, 2 중 1개로 나누어 떨어지면 그 숫자로 나눈다.
# 정수 x에서 1을 뺀다
# 위의 4가지 연산을 사용 할 수 있음. 적절히 사용하여 값을 1로 만드는 최소 횟수

import sys

n = int(sys.stdin.readline())

dp = [0] * 30001

# ?
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    print('ago', dp)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i //2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i //3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i //5] + 1)
    print('after', dp)

