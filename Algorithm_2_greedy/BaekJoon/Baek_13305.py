# 백준 13305번
n, k = input(), list(map(int, input().split()))
price = list(map(int, input().split()))
print(k, price)
min_p = price[0]
total_price = 0
total_far = 0

for i in range(len(price) - 1):
    if min_p > price[i]:
        min_p = price[i]
for v in k:
    total_far += v

for j in range(len(k)):
    if price[j] != min_p:
        total_price += k[j] * price[j]
        total_far -= k[j]
    else:
        total_price += total_far * price[j]
        break

print(total_price)
