# 4. 병합 정렬

# 핵심 아이디어 : 일단 반으로 나누고 나중에 합친다.

# 퀵 정렬과 유사하게 분할 정렬 방법을 사용한다.
# 하지만 퀵 정렬이 피벗 값에 따라 시간 복잡도가 달라진다는 점과 비교하여
# 병합 정렬은 정확히 반 반씩 나누어서 진행되기 때문에 시간 복잡도를 보장한다.

arr = [7, 6, 5, 8, 3, 5, 9, 1]


# arr = [6,1,23,7,19, 200, 27,2]


def merge_sort(arr):
    """ 오름차순 병합 정렬을 실행합니다. """
    n = len(arr)
    # 만약에 arr의 원소가 1개라면 바로 리턴
    if n <= 1:
        return

    # 이 밑의 코드는 리스트의 원소가 2개 이상일 때부터 실행된다.
    # 나눌 중간 점을 정하야 하니 2로 나눈다.
    mid = n // 2
    # 왼쪽 그룹은 index 0 ~ index mid 까지
    left_group = arr[:mid]
    # 오른쪽 그룹은 index mid ~ len(arr) 까지
    right_group = arr[mid:]

    # 정렬 과정이 들어가기 전, 병합 정렬의 아이디어 대로 원소를 잘게 잘게 나눈다.
    merge_sort(left_group)
    merge_sort(right_group)

    # 리스트를 나누었다면, 나눈 그룹을 정렬 후 넣어야 하니 시작 인덱스 left, right를 설정한다.
    left = 0
    right = 0
    # 위에서 left, right 중에서 작은 것을 넣어야 하니 넣어야 할 list의 인덱스 now를 정한다.
    now = 0

    # left, 또는 right의 리스트를 돌며 더 작은 것을 넣을 것
    # left, 또는 right 중 한 리스트를 모두 넣을 때 까지 밑의 while문을 돈다.
    while left < len(left_group) and right < len(right_group):
        # 만약 left의 원소가 right의 원소보다 작다면
        if left_group[left] < right_group[right]:
            # arr의 now인덱스에 left의 해당 원소 (left 인덱스)를 삽입
            arr[now] = left_group[left]
            # 삽입 했으니 left의 인덱스를 1 이동
            left += 1
            # now도 삽입이 완료 되었으니 now의 인덱스도 1 이동
            now += 1
        # 만약 right의 원소가 left의 원소보다 더 작다면
        else:
            # arr의 now인덱스의 right의 해당 원소 (right인덱스)를 삽입
            arr[now] = right_group[right]
            # 삽입 했으니 right의 인덱스를 1 이동
            right += 1
            # now도 삽입이 완료 되었으니 인덱스를 1 이동
            now += 1

    # 위의 while문은 left, right 두 개의 리스트 중 한 개가 모두 삽입이 완료 되었다면 종료된다.
    # 따라서 left, right 중 남은 리스트의 원소를 넣어주는 과정을 작성한다.
    # 만약 left가 남았으면 left를 끝까지 도는데
    while left < len(left_group):
        # 위에서 삽입 후에 실행 했던 과정 반복
        # 대신, 나눠진 리스트는 정렬이 되었다고 가정되므로 비교과정을 생략하고 바로 삽입 후 인덱스를 바꿔준다.
        arr[now] = left_group[left]
        left += 1
        now += 1
    # right가 남았으면 right를 끝까지 돈다.
    while right < len(right_group):
        arr[now] = right_group[right]
        right += 1
        now += 1


merge_sort(arr)

print(arr)

