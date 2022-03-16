# 백준 2752번
# 숫자 세 개를 오름차순으로 정렬한다.
# 숫자 세 개가 주어 졌을때 출력하는 프로그램

arr = list(map(int, input().split()))

def sol(arr, start, end):
    if start >= end:
        return
    pivot = start
    i = start + 1
    j = end
    while i <= j:
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
    sol(arr, start, j - 1)
    sol(arr, j + 1, end)

    return arr


print(sol(arr, 0, len(arr)-1))
