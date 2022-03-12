


# 백준 7568번
# n = input()
# arr = []
# for _ in range(int(n)):
#     kg, cm = map(int, input().split())
#     arr.append([kg, cm])
#
# for i in range(len(arr)):
#     rank = 1
#     for j in range(len(arr)):
#         if i == j:
#             continue
#         elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
#             rank += 1
#     print(rank, end=' ')


# 백준 1018번

# n,m = map(int,input().split())
# arr = list()
# for _ in range(int(n)):
#     k = input()
#     arr.append(k)
#
# arr_count = list()
#
#
# for i in range(n-7):
#     for j in range(m-7):
#         for v in range(i, i+8):
#             for h in range(j,j+8):
#
#
#
#


# 백준 1436번
# n = int(input())
#
# count = 0
# i = 665
# while count < n:
#     i += 1
#     if '666' in str(i):
#         count += 1
#
# print(i)

# 백준 2798번

standard = list(map(int, input().split()))
arr = list(map(int, input().split()))

m = 0

for i in arr:
    for j in arr:
        if i != j:
            for h in arr:
                k = i + j + h
                if i != h and j != h and m < k <= standard[1]:
                    m = k
print(m)