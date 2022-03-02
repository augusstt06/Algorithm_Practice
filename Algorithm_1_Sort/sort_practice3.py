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
4
1
3
7
2

# 1) 선택 정렬
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

# 2) 버블 정렬
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


# 3) 삽입 정렬
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

# 4) 퀵 정렬
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
#

# 5) 병합 정렬
# def merge_sort(arr):
#     if len(arr) < 2:
#         return
#
#     middle = len(arr) // 2
#     left_g = arr[:middle]
#     right_g = arr[middle:]
#
#     merge_sort(left_g)
#     merge_sort(right_g)
#
#     left_i = 0
#     right_i = 0
#     merge_i = 0
#
#     while left_i < len(left_g) and right_i < len(right_g):
#         if left_g[left_i] < right_g[right_i]:
#             arr[merge_i] = left_g[left_i]
#             left_i += 1
#             merge_i += 1
#         else:
#             arr[merge_i] = right_g[right_i]
#             right_i += 1
#             merge_i += 1
#     while left_i < len(left_g):
#         arr[merge_i] = left_g[left_i]
#         merge_i += 1
#         left_i += 1
#     while right_i < len(right_g):
#         arr[merge_i] = right_g[right_i]
#         merge_i += 1
#         right_i += 1
#
#     return arr
#
#
# print(merge_sort(arr))

# def merge_sort(arr):
#     if len(arr) < 2:
#         return
#     middle = len(arr) // 2
#     left_group = arr[:middle]
#     right_gruop = arr[middle:]
#
#     merge_sort(left_group)
#     merge_sort(right_gruop)
#
#     left_index = 0
#     right_index = 0
#     merge_index = 0
#     while left_index < len(left_group) and right_index < len(right_gruop):
#         if left_group[left_index] < right_gruop[right_index]:
#             arr[merge_index] = left_group[left_index]
#             left_index += 1
#             merge_index += 1
#         else:
#             arr[merge_index] = right_gruop[right_index]
#             right_index += 1
#             merge_index += 1
#     while left_index < len(left_group):
#         arr[merge_index] = left_group[left_index]
#         merge_index += 1
#         left_index += 1
#     while right_index < len(right_gruop):
#         arr[merge_index] = right_gruop[right_index]
#         right_index += 1
#         merge_index += 1
#
#     return arr
#
#
# print(merge_sort(arr))
