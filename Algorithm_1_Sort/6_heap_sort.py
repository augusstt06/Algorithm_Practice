# 6) 힙 정렬

# 핵심 아이디어 : 힙 구조를 만들어서 데이터를 정렬한다.

# 힙 : 최대, 최솟값을 빠르게 찾기 위해 완전 이진트리를 기반으로 하는 트리

#

# arr = [1, 10, 5, 8, 12, 7, 6, 4, 3, 2, 11, 9]
arr = [7, 6, 5, 8, 3, 5, 9, 1, 6]

# 8
# 7         9
# 6    3      5  5
# 1 6


def heap_sort(arr):
    # heap 구성
    # 여기서 최초로 힙구조를 만들어 준다
    for i in range(len(arr)):
        c = i
        while c != 0:
            # root => 부모값을 뜻함 // i = 0은 어차피 가장 상위니 패스 그 다음 1부터 들어간다.
            root = (c - 1) // 2
            # print(arr, arr[root], arr[c], '루트와 자식 노드 비교')
            # 부모값이 자식 값보다 작으면 자리를 바꿔준다.
            if arr[root] < arr[c]:
                temp = arr[root]
                arr[root] = arr[c]
                arr[c] = temp
            c = root
    print(arr, '최초로 힙정렬 완료')
    # 크기를 줄여가면서 heap 구성
    j = len(arr) - 1
    while j >= 0:
        # 최상위 노드에는 가장 큰 수가 오니 그 수와 가장 끝 노드(제일 작은수)를 먼저 바꿔준다.
        temp = arr[0]
        arr[0] = arr[j]
        arr[j] = temp
        root = 0
        c = 1
        # print(arr,'먼저 상위 노드랑 끝이랑 바꾸ㅁ')
        while c < j:
            c = 2 * root + 1
            print(j,'범위',root,c,'root,c',root, arr, '전')
            # 자식 중 더 큰 값 찾기
            if (c < j - 1) and (arr[c] < arr[c + 1]):
                c += 1
            # 루트보다 자식이 크다면 교환
            if (c < j) and (arr[root] < arr[c]):
                temp = arr[root]
                arr[root] = arr[c]
                arr[c] = temp
            root = c
            print(j, '범위', root, c, 'root,c', root, arr, '후')
        print('탈출')
        j -= 1

    return arr


print(heap_sort(arr))
