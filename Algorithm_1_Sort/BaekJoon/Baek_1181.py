# 백준 1181번
# 알파벳 소문자로 이루어진 n개의 단어가 들어오면
# 단어의 길이가 짧은 것 부터, 길이가 같으면 사전 순으로 정렬
data = int(input())
arr = []
for v in range(data):
    arr.append(input())


def sol(arr):
    answer = sorted(arr)
    print(answer)
    for i in range(len(answer)):
        for j in range(len(answer) - (i+1)):
            if len(answer[j]) > len(answer[j+1]):
                temp = answer[j]
                answer[j] = answer[j+1]
                answer[j+1] = temp
            elif answer[j] == answer[j+1]:
                del answer[j+1]
    print(answer)
    t = 0
    while t < len(answer):
        # print(answer[t])
        t += 1
    return



print(sol(arr))

# def sol(arr):
#     arr.sort()
#     for i in range(len(arr)):
#         for j in range(len(arr) - (i + 1)):
#             if len(arr[j]) > len(arr[j + 1]):
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#     t = 0
#     length = len(arr) - 1
#     print(arr[0])
#     while t < length:
#         if arr[t] == arr[t + 1]:
#             del arr[t + 1]
#             t += 1
#             length -= 1
#
#         t += 1
#         print(arr[t])
#
#     return
#
#
# print(sol(arr))
