# 백준 1707번
import sys

k = int(sys.stdin.readline())

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(v+1)]

    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        arr[x].append(y)
        arr[y].append(x)
    print(arr)
    visited = [0] * (len(arr) -1)

    # def sol(arr):
    #     for i in range(1, len(arr)):
    #