# 영상 문제 : 시각

# 3이 하나라도 포함되는 모든 경우의 수

# 60초 * 60분 * 24

# n = 60 * 60 * 24
# print(n)
#
# print(59*60)
# print(3540 + 59)

# 3599
k = int(input())
count = 0

for i in range(k+1):
    for j in range(60):
        for u in range(60):
            if '3' in str(i) + str(j) + str(u):
                count += 1
print(count)


# print(70 //60)