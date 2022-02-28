# 정렬 예제 1

# 백준 2752번
# 숫자 세 개를 오름차순으로 정렬한다.
# 숫자 세 개가 주어 졌을때 출력하는 프로그램

arr = list(map(int, input().split()))


# 1) 선택 정렬
# def select_sort(arr):
#     for i in range(len(arr)):
#         min_num = 9999
#         min_index = 0
#         for j in range(i,len(arr)):
#             if min_num > arr[j]:
#                 min_num = arr[j]
#                 min_index = j
#         temp = arr[i]
#         arr[i] = min_num
#         arr[min_index] = temp
#     return arr
#
#
# print(select_sort(arr))


# 2) 버블 정렬
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - (i + 1)):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#
#     return arr
#
#
# print(bubble_sort(arr))

# 3) 삽입 정렬
# def insert_sort(arr):
#     for i in range(len(arr)):
#         j = i
#         while j > 0 and arr[j] < arr[j - 1]:
#             temp = arr[j]
#             arr[j] = arr[j - 1]
#             arr[j - 1] = temp
#             j -= 1
#     return arr
#
#
# print(insert_sort(arr))

# 4) 퀵 정렬
# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#     pivot = start
#     i = start + 1
#     j = end
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
#     quick_sort(arr, start, j - 1)
#     quick_sort(arr, j + 1, end)
#
#     return arr
#
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

    left_i = 0
    right_i = 0
    merge_i = 0

    while left_i < len(left_g) and right_i < len(right_g):
        if left_g[left_i] < right_g[right_i]:
            arr[merge_i] = left_g[left_i]
            left_i += 1
            merge_i += 1
        else:
            arr[merge_i] = right_g[right_i]
            right_i += 1
            merge_i += 1

    while left_i < len(left_g):
        arr[merge_i] = left_g[left_i]
        left_i += 1
        merge_i += 1
    while right_i < len(right_g):
        arr[merge_i] = right_g[right_i]
        right_i += 1
        merge_i += 1

    return arr

print(merge_sort(arr))