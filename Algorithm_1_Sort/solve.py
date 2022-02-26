def quick_sort(arr, start, end):
    # 만약 원소가 1개라면 그냥 리턴
    if start >= end:
        return arr
    # 피벗 값, 왼오 시작점, 오왼 시작 점을 정한다.
    pivot = start
    i = start + 1
    j = end

    # 왼오 시작점이 오왼 시작점 보다 커지면 이 반복문을 탈출
    while i <= j:
        # 왼오 시작점이 오왼 시작점 범위 내에 있고, 현재 시작점으로부터 탐색하는 값이 피벗 점의 값보다 작다면 한칸씩 이동하며 탐색
        # 피벗점의 값보다 큰값을 찾는다면 해당 점의 인덱스를 i로 반환하여 탈출
        while i <= end and arr[i] <= arr[pivot]:
            i += 1
        # 오왼 시작점이 왼오 시작점의 범위 내에 있고, 현재 시작점으로부터 탐색하는 값이 피벗 점의 값보다 크다면 한칸씩 이동하며 탐색
        # 피벗점 = start인데 피벗점은 정렬하지 않으니 해당 점은범위에서 제외한다.
        # 피벗점의 값보다 작은 값을 찾는다면 해당 점의 인덱스를 j로 반환하여 탈출
        while j > start and arr[j] >= arr[pivot]:
            j -= 1
        # 만약 i가 j보다 커지면 ==> 두 점이 엇갈린다면 j의 자리(작은 값을 찾는 j)와 피벗점의 자리를 바꾼다. ==> 이 경우 상위 while문의 탈출조건을 충족하여 while문을 탈출한다.
        if i > j:
            temp = arr[j]
            arr[j] = arr[pivot]
            arr[pivot] = temp
        # 만약 i가 j보다 작다면 두 점의 위치를 바꾼다. ==> 이 경우 다시 상위 whil문을 반복함
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    # 상위 while문을 탈출하였다면 ==> i > j가 충족되어 피벗값과 j를 바꿨다면
    # 바꾼 피벗 점의 위치를 기준으로 왼쪽, 오른쪽의 피벗점을 다시 정하여 정렬해야 하기 때문에 재귀함수를 호출한다.

    # 피벗점 왼쪽의 그룹의 종료점 == 피벗값이 이전 j값과 바뀌었기 때문에 j-1까지 정렬을 시행한다.
    quick_sort(arr, start, j-1)
    # 피벗점 오른쪽의 그룹의 시작점 == 피벗값이 이전 j값과 바뀌었기 때문에 j+1부터 정렬을 시행한다.
    quick_sort(arr, j+1, end)

    # 최종적으로 정렬이 완료되면 정렬된 arr을 리턴
    return arr


print(quick_sort(arr, 0, len(arr)-1))