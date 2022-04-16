# 화폐구성

# n가지 종류의 화폐를 최소한으로 이용하여 가치의 합이 m이 되도록 하는 최소한의 경우의 수
# 2,3원 화폐가 있을때는 3원 5개를 사용하는 것이 최소한의 경우의수
# 불가능할 경우는 -1 출력

import sys

n, m = map(int, sys.stdin.readline().split(' '))
arr = list()
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    # 현재의 i부터 타겟 가격까지 반복문을 돈다.
    for j in range(arr[i], m+1):
        # 만약 현재의 j가격 - 현재의 i를 뺀 경우의 수가 10001이 아니라면 : 제작이 가능하다면
        # == 현재 가격 - i의  데이터가 제작이 가능했다면
        if dp[j-arr[i]] != 10001:
            # 현재의 가격 경우의수와 현재 가격 - i의  데이터에 i를 더한 경우의 수 중 미니멈을 뽑
            dp[j] = min(dp[j], dp[j-arr[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

print(dp)