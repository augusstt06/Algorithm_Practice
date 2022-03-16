# 백준 2798번

standard = list(map(int, input().split()))
arr = list(map(int, input().split()))

m = 0

for i in arr:
    for j in arr:
        if i != j:
            for h in arr:
                k = i + j + h
                if i != h and j != h and m < k <= standard[1]:
                    m = k
print(m)