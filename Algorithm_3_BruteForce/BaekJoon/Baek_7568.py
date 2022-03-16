# 백준 7568번
n = input()
arr = []
for _ in range(int(n)):
    kg, cm = map(int, input().split())
    arr.append([kg, cm])

for i in range(len(arr)):
    rank = 1
    for j in range(len(arr)):
        if i == j:
            continue
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end=' ')
