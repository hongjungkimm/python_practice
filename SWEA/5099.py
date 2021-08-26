from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split())) # 까르보나라 피자, 페퍼로니 피자, 불고기 피자, 시카고 피자 ......
    pizza2 = list(range(1, M+1)) # 피자의 인덱스를 넣어준 리스트
    queue1 = deque() # 피자의 화덕
    queue2 = deque() # 피자 인덱스의 화덕
    for i in range(N): # 화덕 받침 수만큼 화덕에 피자 & 피자 인덱스 추가
        queue1.append(pizza.pop(0))
        queue2.append(pizza2.pop(0))
    flag = False # stop sign
    while True:
        for _ in range(N):
            if len(queue1) < 2: # 화덕에 피자가 하나만 남으면
                flag = True # part stop sign
                break
            a = queue1.popleft() # 화덕의 1번째 피자 위치
            b = queue2.popleft() # 화덕의 1번째 피자 인덱스 위치
            if a == 0: # 만약 피자의 치즈가 녹았고
                if pizza: # 아직 화덕에 넣어줄 피자가 남았다면
                    queue1.appendleft(pizza.pop(0)) # 화덕에 피자 추가
                    queue2.appendleft(pizza2.pop(0)) # 화덕에 피자 인덱스 추가
            else:
                queue1.append(a//2) # 피자의 치즈가 녹지 않았다면 양을 현재의 치즈 // 2 로 해서 화덕의 마지막 순서로
                queue2.append(b) # 피자 인덱스는 그냥 그대로 화덕의 마지막 순서로
        if flag: # whole stop sign
            break

    print('#{0} {1}'.format(tc, *queue2))