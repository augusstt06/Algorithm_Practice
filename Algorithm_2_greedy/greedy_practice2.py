# 백준 5585
# 잔돈 500, 100, 50, 10, 5, 1
# 잔돈의 갯수 최소화
# 1000원을 냈을떄 거스름돈임

# price = 1000 - int(input())
# change = [500, 100, 50, 10, 5, 1]
#
# answer = 0
#
# for i in change:
#     if price > i == 0:
#         continue
#     num = price // i
#     price -= num * i
#     answer += num
#
# print(answer)


# 백준 2839번
# n kg의 설탕, 3, 5 kg의 단위
# ==> 최대한 적은 봉지로 가져 갈 수 있도록

# n = int(input())
# answer = 0
# arr = list()
# for i in range((n // 5)+1):
#     copy = n
#     k = copy - (5 * i)
#     three = k // 3
#     copy -= i*5 + (three * 3)
#     if copy == 0:
#         arr.append(i + three)
#
# arr.sort()
# if len(arr) == 0:
#     print(-1)
# else:
#     print(arr[0])
