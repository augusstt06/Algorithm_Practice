# 백준 11047번

n, k = map(int, input().split())

data = [int(input()) for _ in range(n)]
data.reverse()


count = 0
i = 0
while i < n:
    num = k // data[i]
    if data[i] > k:
        i += 1
        continue
    else:
        if num > 0:
            count += num
            k -= num * data[i]
            i += 1
        else:
            i += 1

print(count)