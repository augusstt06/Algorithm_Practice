# 6) 힙 정렬

# 핵심 아이디어 : 힙 구조를 만들어서 데이터를 정렬한다.

# 힙 : 최대, 최솟값을 빠르게 찾기 위해 완전 이진트리를 기반으로 하는 트리

#

# arr = [1, 10, 5, 8, 12, 7, 6, 4, 3, 2, 11, 9]
arr = [7, 6, 5, 8, 3, 5, 9, 1, 6]


def heap_sort(arr):
    # heap 구성
    for i in range(len(arr)):
        c = i
        while c != 0:
            # root => 부모값을 뜻함 // i = 0은 어차피 가장 상위니 패스 그 다음 1부터 들어간다.
            root = (c - 1) // 2
            # 부모값이 자식 값보다 작으면 자리를 바꿔준다.
            if arr[root] < arr[c]:
                temp = arr[root]
                arr[root] = arr[c]
                arr[c] = temp
            c = root

    # 크기를 줄여가면서 heap 구성
    j = len(arr) - 1
    while j >= 0:
        print(arr, j, '두번째 while 시작 전')
        temp = arr[0]
        arr[0] = arr[j]
        arr[j] = temp
        root = 0
        c = 1
        while c < j:
            c = 2 * root + 1
            print(c, 'c')
            # 자식 중 더 큰 값 찾기
            if (c < j - 1) and (arr[c] < arr[c + 1]):
                c += 1
            # 루트보다 자식이 크다면 교환
            if (c < j) and (arr[root] < arr[c]):
                temp = arr[root]
                arr[root] = arr[c]
                arr[c] = temp
            root = c
        j -= 1

    return arr


print(heap_sort(arr))
