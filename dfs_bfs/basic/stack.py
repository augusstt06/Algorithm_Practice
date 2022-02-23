# Stack : 나중에 넣은 데이터가 먼저 반환
# 데이터를 하나하나 쌓는 개념 ==> 가장 먼저 들어간 데이터는 가장 나중에 반환, 가장 나중에 들어간 데이터는 가장 먼저 반환

# 리스트를 활용하여 스택구조로 데이터 처리가 가능하다.
# 데이터의 입력 : push ===> append()
# 데이터의 출력 : pop ====> pop()
# * pop으로 출력한 데이터는 리스트내에서 사라지고 리턴된다 *

msg = input('문자를 입력하세요 : ')
msg_list = list(msg)
print(msg_list)
for i in range(len(msg_list)):
    print(msg_list.pop(), '출력값')
    print(msg_list, '잔존 리스트')