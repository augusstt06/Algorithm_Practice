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
