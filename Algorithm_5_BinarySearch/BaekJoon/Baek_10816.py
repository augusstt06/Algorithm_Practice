# 백준 10816번

import sys
from bisect import bisect_left, bisect_right

n = int(input())
arr_card = list(map(int, sys.stdin.readline().split()))
arr_card.sort()

m = int(input())
arr_count = list(map(int, sys.stdin.readline().split()))

def sol(arr, num):
    left = bisect_left(arr, num)
    right = bisect_right(arr, num)
    return print(right - left, end=' ')

for i in arr_count:
    sol(arr_card, i)

