# 4. 병합 정렬

# 핵심 아이디어 : 일단 반으로 나누고 나중에 합친다.

# 퀵 정렬과 유사하게 분할 정렬 방법을 사용한다.
# 하지만 퀵 정렬이 피벗 값에 따라 시간 복잡도가 달라진다는 점과 비교하여
# 병합 정렬은 정확히 반 반씩 나누어서 진행되기 때문에 시간 복잡도를 보장한다.

arr = [7, 6, 5, 8, 3, 5, 9, 1]


def merge_sort(arr):
    """ 오름차순 병합 정렬을 실행합니다. """
    n = len(arr)

    if n <= 1:
        return

    mid = n // 2
    left_group = arr[:mid]
    right_group = arr[mid:]

    merge_sort(left_group)
    merge_sort(right_group)

    left = 0
    right = 0
    now = 0

    while left < len(left_group) and right < len(right_group):
        if left_group[left] < right_group[right]:
            arr[now] = left_group[left]
            left += 1
            now += 1
        else:
            arr[now] = right_group[right]
            right += 1
            now += 1

    while left < len(left_group):
        arr[now] = left_group[left]
        left += 1
        now += 1

    while right < len(right_group):
        arr[now] = right_group[right]
        right += 1
        now += 1


merge_sort(arr)

print(arr)
