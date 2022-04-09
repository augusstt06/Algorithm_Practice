# 백준 1920
import sys

n = int(input())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_a.sort()
m = int(input())

arr_target = list(map(int, sys.stdin.readline().split()))

def sol(arr, num):
    start = 0
    end = len(arr)-1

    count = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            count += 1
            break
        if arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    return print(count)

for i in arr_target:
    sol(arr_a, i)
