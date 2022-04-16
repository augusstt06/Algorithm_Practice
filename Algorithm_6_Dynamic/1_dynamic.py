# Dynamic Programming
# 이미 계산된 결과를 별도의 메모리에 저장하여 다시 계산하지 않게끔 함으로써 효율성을 증대 시킬수 있다.

# 예시 - 피보나치 수열
# 인접한 항들 사이의 관계식을 정의할 수 있다
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 탑다운(하향식) - 메모이제이션
# 한번 계산한 결과를 메모리 공간에 메모하는 기법 (캐싱)
# 바텀업(상향식) - 반복문 사용

# 캐싱을 사용하영 피보나치 풀기

memo = [0] * 100

def fibo_m(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산된 적이 있다면 그 값을 리턴하고
    if memo[x] != 0:
        return memo[x]
    # 그게 아니라면 다시 계산하여 리스트에 넣고 그 값을 리턴한다.
    memo[x] = fibo(x-1) + fibo(x-2)
    return memo[x]

print(fibo_m(4))

