# 백준 2750번
# 첫째 줄에 수의 갯수 (1<= n <=1000), 둘째 줄 부터는 숫자가 주어진다
# 이 수들은 절대값이 1000보다 작거나 같다. 중복은 없다
import sys

num = int(sys.stdin.readline())
arr = list()

for v in range(num):
    arr.append(int(sys.stdin.readline().strip()))


# 1) 선택 정렬
# def select_sort(num, arr):
#     for i in range(num):
#         min_num = 9999
#         min_index = 0
#
#         for j in range(i,num):
#
#             if min_num > arr[j]:
#                 min_num = arr[j]
#                 min_index = j
#
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#
#     return '선택 정렬 완료', arr
#
#
# print(select_sort(num, arr))


# 2) 버블 정렬
# def bubble_sort(num, arr):
#     for i in range(num):
#         for j in range(num-(i+1)):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#
#     return '버블 정렬 완료', arr
#
#
# print(bubble_sort(num, arr))

# 5 2 3 4 1

# 3) 삽입 정렬
# def insert_sort(num, arr):
#     for i in range(num):
#         j = i
#         # print(i, arr)
#         while j > 0:
#             if arr[j] < arr[j - 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j - 1]
#                 arr[j - 1] = temp
#             print(arr,j)
#             j -= 1
#         # print(arr)
#     return '삽입 정렬 완료', arr
#
#
# print(insert_sort(num, arr))

# 4) 퀵 정렬

# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     i = start + 1
#     j = end
#
#     while i <= j:
#         while i <= end and arr[i] <= arr[pivot]:
#             i += 1
#         while j > start and arr[j] >= arr[pivot]:
#             j -= 1
#
#         if i > j:
#             temp = arr[j]
#             arr[j] = arr[pivot]
#             arr[pivot] = temp
#         else:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#
#     quick_sort(arr, j+1, end)
#
#     quick_sort(arr, start, j-1)
#
#     return arr
#
# print(quick_sort(arr, 0, len(arr)-1))

# 5) 병합 정렬
def merge_sort(arr):
    if len(arr) < 2:
        return
    middle = len(arr) // 2
    left_g = arr[:middle]
    right_g = arr[middle:]

    merge_sort(left_g)
    merge_sort(right_g)

    left_index = 0
    right_index = 0
    merge_index = 0

    while left_index < len(left_g) and right_index < len(right_g):
        if left_g[left_index] < right_g[right_index]:
            arr[merge_index] = left_g[left_index]
            left_index += 1
            merge_index += 1
        else:
            arr[merge_index] = right_g[right_index]
            right_index += 1
            merge_index += 1

    while left_index < len(left_g):
        arr[merge_index] = left_g[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right_g):
        arr[merge_index] = right_g[right_index]
        right_index += 1
        merge_index += 1
    return arr


print(merge_sort(arr))
