# 백준 1436번
n = int(input())

count = 0
i = 665
while count < n:
    i += 1
    if '666' in str(i):
        count += 1

print(i)