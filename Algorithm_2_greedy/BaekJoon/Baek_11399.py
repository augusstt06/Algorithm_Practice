# 백준 11399번

n = int(input())
data = sorted(list(map(int, input().split())))


def greedy(arr):
    answer = 0
    for i in range(1,len(arr)+1):
        j = 0
        time = 0
        while j < i:
            time += arr[j]
            j += 1
        answer += time
    return answer


print(greedy(data))

# n = int(input())
# data = sorted(list(map(int, input().split())))
# answer = 0
# for i in range(1, len(data)+1):
#     j = 0
#     time = 0
#     while j < i:
#         time += data[j]
#         j += 1
#     answer += time
#     print(answer)
# print(answer)