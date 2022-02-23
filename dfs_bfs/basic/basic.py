# stack : 선입 후출

stack = [5]

stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1], '최상단 원소부터 출력')
print(stack, '최하단 원소부터 출력')

# queue : 선입 선출

from collections import deque

queue = deque()

# 오른쪽 => 왼쪽 들어온다 생각하면 편함

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()

queue.append(1)
queue.append(4)

queue.popleft()
print(queue, '먼저 들어온 순서대로 출력')
queue.reverse()
print(queue, '나중에 들어온 원소부터 출력')


# 재귀 함수 => 종료 조건 필히 명시 :: 마치 stack과 비슷하게 작동


def recursive_function(i):
    if i == 10:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출 합니다')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다')


recursive_function(1)


# 팩토리얼 구현 예제

# 반복문 사용


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀 함수 사용
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print('반복문', factorial_iterative(5))
print('재귀', factorial_recursive(5))

# 유클리드 호제법
# 두 자연수 a,b에 대하여 (a > b) a를 b로 나눈 나머지를 r
# 이 a,b의 최대공약수는 b,r의 최대공약수와 같다.
# ===> 재귀를 통하여 최초 a % b = r 을 반복한다.


def gcd(a,b):
    r = a % b
    if r == 0:
        # a가 b의 배수라면 바로 b를 리턴
        return b
    else:
        # 배수가 아니라면 a,b중 더 작은 값인 b와 나눈 나머지 r을 다시 gcd 함수의 매개 변수로 넣어서 호출
        return gcd(b, r)


print(gcd(192, 162))

