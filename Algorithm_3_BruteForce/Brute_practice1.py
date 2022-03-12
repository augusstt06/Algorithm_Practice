# 백준 2798번

# standard = list(map(int, input().split()))[1]
# arr = list(map(int, input().split()))
#
# ave = standard // 3
# count = 0
# dif = abs(ave - arr[-1])
#
# for j in arr:
#     if abs(ave - j) < dif:
#         dif = ave - j
# for h in arr:


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
n,m = input().split()
arr = list()
for _ in range(int(n)):
    k = input()
    arr.append(k)
print(arr)