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
