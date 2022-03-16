# 백준 5585
# 잔돈 500, 100, 50, 10, 5, 1
# 잔돈의 갯수 최소화
# 1000원을 냈을떄 거스름돈임

price = 1000 - int(input())
change = [500, 100, 50, 10, 5, 1]

answer = 0

for i in change:
    if price > i == 0:
        continue
    num = price // i
    price -= num * i
    answer += num

print(answer)
