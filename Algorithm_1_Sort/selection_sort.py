# 1. 선택 정렬
# 정렬할 요소를 돌면서 가장 작은 것을 선택 해서 제일 앞으로 보낸다
# 정렬할 요소의 리스트를 1번째~마지막, 2번째~마지막 ... 순으로 순차적으로 돌면서
# 가장 작은 값을 앞으로 보낸다 (배열의 위치를 바꾼다)

# 선택 정렬 구현 (오름 차순으로 구현 한다)

def f_select(arr):
    for i in range(len(arr)):
        # 돌아야 할 범위 안의 최솟값을 찾기 위해 min_num이라는 변수 생성
        # 최솟값을 찾았다면 그 값의 인덱스를 바꿔야 하므로 인덱스를 담을 변수 생성
        min_num = 9999
        index_num = 0
        # 밑의 for문은 i의 다음 요소를 다 확인한다.
        for j in range(i, len(arr)):
            # 만약에 현재의 min_num이 현재 돌고 있는 요소값보다 크다면
            if min_num > arr[j]:
                # min_num을 현재 요소값으로 갱신한다.
                min_num = arr[j]
                # 그리고 갱신한 요소값의 인덱스를 index_num으로 갱신
                index_num = j
        # i를 기준으로 그 후의 요소들을 다 확인 했다면

        # 최소값의 위치를 앞으로 보내야 하므로 temp라는 변수를 생성하여 현재 i의 요소값을 담는다
        temp = arr[i]
        # 현재 i의 요소값 = 위에서 최종적으로 갱신한 index_num의 요소값
        arr[i] = arr[index_num]
        # 위에서 현재 i의 요소값이 갱신 되었으므로 현재 i값을 바꾼 index_num의 자리에 넣어줘야 한다. index_num의 요소값 = 위에서 생성한 temp값
        arr[index_num] = temp

    #     이 과정을 i가 주어진 범위를 다 돌 때까지 반복한다.
    print(arr)


# arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
# arr = [11, 12, 15, 16, 13, 18, 14, 17, 20, 19]
arr = [16, 7, 12, 11, 8, 10, 9, 15, 13, 14]

print(f_select(arr))
