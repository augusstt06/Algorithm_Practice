# 정렬 예제 3

# 백준 2751번
# 첫째 줄에 수의 갯수 (1<= n <=1000), 둘째 줄 부터는 숫자가 주어진다
# 이 수들은 절대값이 1,000,000보다 작거나 같다. 중복은 없다
# 오름차순으로 정렬하라

import sys

num = int(sys.stdin.readline())
arr = list()

for v in range(num):
    arr.append(int(sys.stdin.readline().strip()))


# 5
# 5
# 4
# 1
# 2
# 3
# 선택 정렬
# def select_sort(arr):
#     for i in range(len(arr)):
#         min_num = 99999999
#         min_index = 0
#         for j in range(i, len(arr)):
#             if min_num > arr[j]:
#                 min_num = arr[j]
#                 min_index = j
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#
#     return arr
#
# def select_sort(arr):
#     for i in range(len(arr)):
#         min_num = arr[i]
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if min_num > arr[j]:
#                 min_num = arr[j]
#                 min_index = j
#
#         temp = arr[i]
#         arr[i] = min_num
#         arr[min_index] = temp
#     return arr

# print(select_sort(arr))

# 버블 정렬
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-(i+1)):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#     return arr
#
# print(bubble_sort(arr))


# 삽입 정렬
# def insert_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j] < arr[j - 1]:
#             temp = arr[j]
#             arr[j] = arr[j - 1]
#             arr[j - 1] = temp
#             j -= 1
#     return arr
#
# print(insert_sort(arr))

# 퀵 정렬
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    i = start + 1
    j = end
    while i <= j :
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
        while j > start and arr[j] >= arr[pivot]:
            j -= 1

        if i > j:
            temp = arr[j]
            arr[j] = arr[pivot]
            arr[pivot] = temp
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    quick_sort(arr, start, j - 1)
    quick_sort(arr, j + 1, end)

    return arr


print(quick_sort(arr,0, len(arr)-1))

