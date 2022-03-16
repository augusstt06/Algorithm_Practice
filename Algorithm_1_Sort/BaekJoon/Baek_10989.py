# 백준 10989
# n개의 수가 주어졌을때 오름차순으로 정렬하시오
data = int(input())
arr = []
for v in range(data):
    arr.append(int(input()))


def sol(arr):
    n = len(arr)
    if n <= 1:
        return
    mid = n // 2
    left_group = arr[:mid]
    right_group = arr[mid:]

    sol(left_group)
    sol(right_group)

    left_index = 0
    right_index = 0
    merge_index = 0
    while left_index < len(left_group) and right_index < len(right_group):
        if left_group[left_index] < right_group[right_index]:
            arr[merge_index] = left_group[left_index]
            left_index += 1
            merge_index += 1
        else:
            arr[merge_index] = right_group[right_index]
            right_index += 1
            merge_index += 1
    while left_index < len(left_group):
        arr[merge_index] = left_group[left_index]
        left_index += 1
        merge_index += 1
    while right_index < len(right_group):
        arr[merge_index] = right_group[right_index]
        right_index += 1
        merge_index += 1

    return arr


print(sol(arr))