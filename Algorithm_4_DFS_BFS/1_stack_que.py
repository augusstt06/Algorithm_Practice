# Stack : 나중에 넣은 데이터가 먼저 반환
# https://somjang.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack
# 데이터를 하나하나 쌓는 개념 ==> 가장 먼저 들어간 데이터는 가장 나중에 반환, 가장 나중에 들어간 데이터는 가장 먼저 반환

# 리스트를 활용하여 스택구조로 데이터 처리가 가능하다.
# 데이터의 입력 : push ===> append()
# 데이터의 출력 : pop ====> pop()
# * pop으로 출력한 데이터는 리스트내에서 사라지고 리턴된다 *

# stack 예시
# msg = input('문자를 입력하세요 : ')
# msg_list = list(msg)
# print(msg_list)
# for i in range(len(msg_list)):
#     print(msg_list.pop(), '출력값')
#     print(msg_list, '잔존 리스트')

# 클래스를 사용한 구현

class Stack:
    def __init__(self):
        self.stack = []

    # stack에 data를 삽입 시
    def push(self, data):
        self.stack.append(data)

    # stack에 data를 꺼낼시 ==> 가장 마지막에 삽입한 data를 꺼내야 하기 떄문에 pop 메소드를 이용한다.
    def pop(self):
        pop_object = None
        # 만약 stack에 data가 없다면 stack이 비어있다는 문자열을 return하고 stop
        if self.is_empty():
            print('Stack List is Empty!')
        # data가 있다면 가장 마지막에 삽입된 데이터를 꺼내서 pop_object 변수에 할당하여 return한다.
        else:
            pop_object = self.stack.pop()
        return pop_object

    # pop 함수에서 사용했던 is_empty라는 메소드를 추가한다.
    # 이 메소드의 기본 return값은 False이지만 stack에 data가 없다면 True로 바뀐다.
    # 이 Boolean값을 이용하여 stack에 data가 있는지 없는지 확인.
    def is_empty(self):
        empty = False
        if len(self.stack) == 0:
            empty = True
        return empty


# class Node:
#     def __init__(self):


# Queue : 먼저 넣은 데이터가 먼저 반환  ( Stack과 반대되는 개념 )
# 데이터를 줄 세워서 입력 및 저장하는 식 (양쪽이 뚫려있는 통에 한 개씩 삽입한다고 생각)

# 리스트를 활용해 구현
# 데이터의 입력 : push ===> append() //// 데이터를 삽입하는 과정은 enqueue라고 한다.
# 데이터의 출력 : get ====> pop(0) //// 데이터를 꺼내는 과정을 dequeue라고 한다. 이 경우, queue가 비어있는지 확인이 필요
# 가장 먼저 입력된 데이터를 출력해야 하므로 리스트의 0번째 인덱스를 출력한다.

# que 예시

# arr = [1, 2, 3, 4, 5]
#
# print(arr)
#
# print(arr.pop(0))
# print(arr.pop(0))
#
# print(arr)

# 하지만 pop으로 출력 후 데이터를 인덱스 1씩 당겨줘야 하므로 시간복잡도 측면에서 비효율적
# deque : 데이터를 양방향에서 추가/제거할수 있는 자료구조
# popleft() 메서드를 이용하여 첫번째 데이터를 제거 할 수 있음

# from collections import deque
#
# queue = deque([1, 2, 3])
# queue.append(4)
# queue.append(5)
# print(queue)
#
# print(queue.popleft())
# print(queue.popleft())
#
# print(queue)

# queue 자료 형태를 구현 하기 적합 하다
# appendleft() :왼쪽으로 원소 추가
# clear() : deque안의 모든 요소 제거
# rotate(x) : deque안의 요소를 x만큼 이동시킨다 (인덱스 변화) ==  회전


# 클래스를 사용한 구현

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        dequeue_object = None
        if self.is_empty():
            print('Queue List is Empty Now!')
        else:
            dequeue_object = self.queue[0]
            self.queue = self.queue[1:]
        return dequeue_object

    def peek(self):
        peek_object = None
        if self.is_empty():
            print('Queue List is Empty Now!')
        else:
            peek_object = self.queue[0]
        return peek_object

    def is_empty(self):
        isempty = False
        if len(self.queue) == 0:
            isempty = True
        return isempty


# from collections import deque
# que = deque()
# que.append(1)
# que.append(2)
# que.popleft()
# print(que)