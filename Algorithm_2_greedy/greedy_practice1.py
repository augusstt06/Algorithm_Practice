# 백준 11399번

# n = int(input())
# data = sorted(list(map(int, input().split())))
#
#
# def greedy(arr):
#     answer = 0
#     for i in range(1,len(arr)+1):
#         j = 0
#         time = 0
#         while j < i:
#             time += arr[j]
#             j += 1
#         answer += time
#     return answer
#
#
# print(greedy(data))

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


# 백준 11047번

# n, k = map(int, input().split())
#
# data = [int(input()) for _ in range(n)]
# data.reverse()
#
#
# count = 0
# i = 0
# while i < n:
#     num = k // data[i]
#     if data[i] > k:
#         i += 1
#         continue
#     else:
#         if num > 0:
#             count += num
#             k -= num * data[i]
#             i += 1
#         else:
#             i += 1
#
# print(count)


# 백준 1931번
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# data.sort(key=lambda x: (x[1], x[0]))
# i = 1
# answer = [data[0]]
# while i < len(data):
#     if answer[-1][1] <= data[i][0]:
#         answer.append(data[i])
#         i += 1
#     else:
#         i += 1
# n = len(answer)
# print(n)

# 범위가 n이 100000이기 때문에 반복문 2개를 돌면 시간복잡도가 너므 높아짐 // 완전탐색 할 이유가 없음
# num = []
# for i in range(len(data)):
# i = 0
# while i < len(data):
#     answer = [data[i]]
#     j = i+1
#     while j < len(data):
#         if answer[-1][1] <= data[j][0]:
#             answer.append(data[j])
#             j += 1
#         else:
#             j += 1
#     num.append(len(answer))
#     i += 1
# print(max(num))


# 백준 1541번
n = input()

# 백준 13305번
