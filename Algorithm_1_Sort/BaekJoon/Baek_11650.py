# 백준 11650
data = int(input())
arr = list()
for v in range(data):
    x, y = map(int, input().split())
    arr.append((x,y))


def sol(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-(i+1)):
            if arr[j][0] > arr[j+1][0]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            elif arr[j][0] == arr[j+1][0] and arr[j][1] > arr[j+1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    for h in arr:
        print(h[0],h[1])


print(sol(arr))
