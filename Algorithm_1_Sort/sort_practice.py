# 백준 1181번
# 알파벳 소문자로 이루어진 n개의 단어가 들어오면
# 단어의 길이가 짧은 것 부터, 길이가 같으면 사전 순으로 정렬
data = int(input())
arr = []
for v in range(data):
    arr.append(input())


def sol(arr):
    answer = sorted(arr)
    print(answer)
    for i in range(len(answer)):
        for j in range(len(answer) - (i+1)):
            if len(answer[j]) > len(answer[j+1]):
                temp = answer[j]
                answer[j] = answer[j+1]
                answer[j+1] = temp
            elif answer[j] == answer[j+1]:
                del answer[j+1]
    print(answer)
    t = 0
    while t < len(answer):
        # print(answer[t])
        t += 1
    return



print(sol(arr))

# def sol(arr):
#     arr.sort()
#     for i in range(len(arr)):
#         for j in range(len(arr) - (i + 1)):
#             if len(arr[j]) > len(arr[j + 1]):
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#     t = 0
#     length = len(arr) - 1
#     print(arr[0])
#     while t < length:
#         if arr[t] == arr[t + 1]:
#             del arr[t + 1]
#             t += 1
#             length -= 1
#
#         t += 1
#         print(arr[t])
#
#     return
#
#
# print(sol(arr))

# 백준 2752번
# 숫자 세 개를 오름차순으로 정렬한다.
# 숫자 세 개가 주어 졌을때 출력하는 프로그램

# arr = list(map(int, input().split()))
#
# def sol(arr, start, end):
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
#     sol(arr, start, j - 1)
#     sol(arr, j + 1, end)
#
#     return arr
#
#
# print(sol(arr, 0, len(arr)-1))

# 백준 10989
# n개의 수가 주어졌을때 오름차순으로 정렬하시오
# data = int(input())
# arr = []
# for v in range(data):
#     arr.append(int(input()))
#
#
# def sol(arr):
#     n = len(arr)
#     if n <= 1:
#         return
#     mid = n // 2
#     left_group = arr[:mid]
#     right_group = arr[mid:]
#
#     sol(left_group)
#     sol(right_group)
#
#     left_index = 0
#     right_index = 0
#     merge_index = 0
#     while left_index < len(left_group) and right_index < len(right_group):
#         if left_group[left_index] < right_group[right_index]:
#             arr[merge_index] = left_group[left_index]
#             left_index += 1
#             merge_index += 1
#         else:
#             arr[merge_index] = right_group[right_index]
#             right_index += 1
#             merge_index += 1
#     while left_index < len(left_group):
#         arr[merge_index] = left_group[left_index]
#         left_index += 1
#         merge_index += 1
#     while right_index < len(right_group):
#         arr[merge_index] = right_group[right_index]
#         right_index += 1
#         merge_index += 1
#
#     return arr
#
#
# print(sol(arr))


# 백준 11650
# data = int(input())
# arr = list()
# for v in range(data):
#     x, y = map(int, input().split())
#     arr.append((x,y))
#
#
# def sol(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-(i+1)):
#             if arr[j][0] > arr[j+1][0]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#             elif arr[j][0] == arr[j+1][0] and arr[j][1] > arr[j+1][1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#     for h in arr:
#         print(h[0],h[1])
#
#
# print(sol(arr))


# 백준 18870
