# 백준 1018번

n,m = map(int,input().split())
arr = list()
for _ in range(int(n)):
    k = input()
    arr.append(k)

answer = list()


for i in range(n-7):
    for j in range(m-7):
        even = 0
        odd = 0
        for v in range(i, i+8):
            for h in range(j,j+8):
                if (v+h) % 2 == 0:
                    if arr[v][h] != 'B':
                        odd += 1
                    elif arr[v][h] != 'W':
                        even += 1
                else:
                    if arr[v][h] != 'B':
                        odd += 1
                    elif arr[v][h] != 'W':
                        even += 1
        answer.append(even)
        answer.append(odd)
