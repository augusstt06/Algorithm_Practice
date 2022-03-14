# Stack : 나중에 넣은 데이터가 먼저 반환
# 데이터를 하나하나 쌓는 개념 ==> 가장 먼저 들어간 데이터는 가장 나중에 반환, 가장 나중에 들어간 데이터는 가장 먼저 반환

# 리스트를 활용하여 스택구조로 데이터 처리가 가능하다.
# 데이터의 입력 : push ===> append()
# 데이터의 출력 : pop ====> pop()
# * pop으로 출력한 데이터는 리스트내에서 사라지고 리턴된다 *


# Queue : 먼저 넣은 데이터가 먼저 반환  ( Stack과 반대되는 개념 )
# 데이터를 줄 세워서 입력 및 저장하는 식 (양쪽이 뚫려있는 통에 한 개씩 삽입한다고 생각)

# 리스트를 활용해 구현
# 데이터의 입력 : push ===> append()
# 데이터의 출력 : get ====> pop(0)
# 가장 먼저 입력된 데이터를 출력해야 하므로 리스트의 0번째 인덱스를 출력한다.


# stack 예시
msg = input('문자를 입력하세요 : ')
msg_list = list(msg)
print(msg_list)
for i in range(len(msg_list)):
    print(msg_list.pop(), '출력값')
    print(msg_list, '잔존 리스트')



# que 예시
arr = [1, 2, 3]

arr.append(4)
arr.append(5)
print(arr)

print(arr.pop(0))
print(arr.pop(0))

print(arr)

# 하지만 pop으로 출력 후 데이터를 인덱스 1씩 당겨줘야 하므로 시간복잡도 측면에서 비효율적
# deque : 데이터를 양방향에서 추가/제거할수 있는 자료구조
# popleft() 메서드를 이용하여 첫번째 데이터를 제거 할 수 있음

from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.append(5)
print(queue)

print(queue.popleft())
print(queue.popleft())

print(queue)

# queue 자료 형태를 구현 하기 적합 하다
# appendleft() :왼쪽으로 원소 추가
# clear() : deque안의 모든 요소 제거
# rotate(x) : deque안의 요소를 x만큼 이동시킨다 (인덱스 변화) ==  회전
