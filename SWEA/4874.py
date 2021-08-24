T = int(input())

for tc in range(1, T+1):
    cal = list(map(str, input().split()))

    cnt_n = 0 # 숫자의 개수
    cnt_c = 0 # 연산자의 개수
    for i in cal[:-1]:
        if i in '+-*/':
            cnt_c += 1
        else:
            cnt_n += 1

    stack = [] # 연산한 숫자를 넣어줄 스택
    error = False # error 여부
    if len(cal) <= 2: # 만약 계산식 안 숫자와 연산자, '.'의 길이가 2이하이면 식이 성립되지 않으므로 error
        error = True
    elif cnt_n - cnt_c == 1: # 만약 숫자가 연산자보다 1개 더 많다면 식은 성립
        for i in range(len(cal)-1): # 맨 뒤의 '.'은 제외하고 반복문
            if cal[i] in '+-*/': # 만약 해당 인덱스의 값이 연산자라면
                if len(stack) < 2: # 하지만, 스택 안의 숫자가 2개 미만이라 연산이 불가능하다면 error
                    error = True
                    break
                a = stack.pop() # 현재 스택의 마지막 숫자
                b = stack.pop() # 현재 스택의 뒤에서 두 번째 숫자
                if cal[i] == '+': # 여기부터 해당 연산자로 계산 후 스택에 추가
                    stack.append(b+a)
                elif cal[i] == '-':
                    stack.append(b-a)
                elif cal[i] == '*':
                    stack.append(b*a)
                else:
                    if a == 0: # 만약 나누는 숫자가 0이면 zerodivision error이므로 error
                        error = True
                        break
                    stack.append(int(b/a))
            else: # 만약 해당 인덱스의 값이 숫자라면 스택에 추가
                stack.append(int(cal[i]))
    else: # 숫자가 연산자보다 1개 더 많지 않다면 식이 성립되지 않으므로 error
        error = True

    if error:
        print('#{0} {1}'.format(tc, 'error'))
    else:
        result = 0
        for i in stack:
            result += i
        print('#{0} {1}'.format(tc, result))