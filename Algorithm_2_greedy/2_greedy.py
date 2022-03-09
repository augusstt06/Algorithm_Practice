# 탐욕법 : 최적의 해를 찾는 알고리즘

# 영상 예제 1 : 1이 될 때 까지
# 내 풀이
# def sol(n, k):
#     count = 0
#     while n != 0:
#         if n == 1:
#             return count
#         elif (n % k) != 0:
#             n -= 1
#             count += 1
#             continue
#         else:
#             n = n / k
#             count += 1
#             continue
#     return count
#
#
# print(sol(25, 3))


# 영상 풀이
# n, k = map(int, input().split())
# result = 0
# # 밑의 코드는 뼤는 연산을 실제로 시행 하지 않고 result라는 변수를 이용하여 한번에 계산
# # 그 이후 나누는 연산만 진행을 한 후 result에 +1을 해주는 방식
# while True:
#     # target = n에 가장 가까운 k의 배수 ==> 나누기 연산을 몇번 하는지 알 수 있음
#     target = (n // k) * k
#     # result = n에서 가장 가까운 k의 배수를 뺸 나머지 ==> -1 연산을 얼마나 해야 하는지 알 수 있다
#     result += (n - target)
#     n = target
#     print(n, result)
#
#     if n < k:
#         break
#     result += 1
#     n //= k
#
#
# result += (n - 1)
# print(result)


# 영상 예제 2 : 곱하기 혹은 더하기
# 내 풀이
# num = input()
# answer = int(num[0])
#
# for i in range(1, len(num)):
#     if answer != 0 and int(num[i]) != 0:
#         answer *= int(num[i])
#     else:
#         answer += int(num[i])
#
# print(answer)

# 영상 풀이
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)