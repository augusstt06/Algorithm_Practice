# 이진 탐색
# 데이터가 정렬된 배열에서 특정한 값을 찾아내는 알고리즘
# 정렬된 배열에서 중간값을 찾아 찾고자 하는 값과 비교하며 탐색한다.
# 반드시 정렬된 배열에서 탐색하여야 한다.


# 반복문을 사용한 구현
def binary(arr, num):
    # 탐색의 시작점과 끝점을 지정한다.
    start = 0
    end = len(arr)-1
    # 반복문을 사용하여 탐색하는데, 시작점이 끝점보다 커지면 반복문을 탈출한다.
    while start <= end:
        # 이진탐색의 핵심인 중간점을 지정한다.
        mid = (start + end) // 2
        # 만약 주어진 배열의 중간값이 찾고자 하는 숫자라면 반복문을 탈출하고 내용을 출력한다.
        if arr[mid] == num:
            return print(f'{num}은 arr배열의 {mid+1} 번째에 위치합니다.')
        # 만약 주어진 배열의 중간값이 주어진 숫자보다 크다면 (즉, 찾고자 하는 숫자는 중간점 왼쪽에 위치한다)
        if arr[mid] > num:
            # 끝점을 현재 중간점-1로 지정하여 다시 반복문을 실행한다. // 현재 중간값의 왼쪽을 다시 탐색
            end = mid - 1
        # 만약 주어진 배열의 중간값이 주어진 숫자보다 작다면 (즉, 찾고자 하는 숫자는 중간점 오른쪽에 위치한다)
        else:
            # 시작점을 현재 중간점+1로 지정하여 다시 반복문을 실행한다. // 현재 중간값의 오른쪽을 다시 탐색한다.
            start = mid + 1
    return None

arr = [0,2,4,6,8,10,10,12,14,16,18]

binary(arr, 10)

# 재귀함수를 사용한 구현
def binary_re(arr, num, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == num:
        return print(f'{num}은 arr배열의 {mid+1} 번째에 위치합니다.')
    if arr[mid] > num:
        return binary_re(arr, num, start, mid - 1)
    else:
        return binary_re(arr, num, mid + 1, end)
binary_re(arr, 8, 0, len(arr)-1)

