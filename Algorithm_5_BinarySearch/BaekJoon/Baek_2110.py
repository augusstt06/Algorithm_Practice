# 백준 2110번
import sys
n, c = map(int, sys.stdin.readline().split())
arr = list()
for _ in range(n):
    arr.append(int(input()))
arr.sort()
# 1 2 4 8 9
def sol(arr):
    start = 1
    end = arr[-1]

    while start <= end:
        mid = (start + end) // 2
        print(mid,'mid')
        temp = arr[0]
        count = 1

        for i in arr:
            if i - temp >= mid:

                temp = i
                count += 1

        if count >= c:
            start = mid + 1
        else:
            end = mid - 1

    return print(end)

sol(arr)
