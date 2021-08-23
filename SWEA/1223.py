for tc in range(1, 11):
    N = int(input())
    cal = input()

    stack1 = []
    chg_cal = []
    for i in range(N):
        if cal[i].isdigit():
            chg_cal.append(cal[i])
        else:
            stack1.append(cal[i])
            while True:
                if len(stack1) <= 1:
                    break
                elif stack1[-2] == '+' and stack1[-1] == '*':
                    break
                elif stack1[-1] == stack1[-2]:
                    chg_cal.append(stack1.pop())
                elif stack1[-2] == '*' and stack1[-1] == '+':
                    chg_cal.append(stack1.pop(-2))

    while stack1:
        chg_cal.append(stack1.pop())

    stack2 = []
    for i in range(N):
        if chg_cal[i].isdigit():
            stack2.append(chg_cal[i])
        else:
            if chg_cal[i]  == '+':
                stack2.append(int(stack2.pop()) + int(stack2.pop()))
            else:
                stack2.append(int(stack2.pop()) * int(stack2.pop()))

    result = 0
    for i in stack2:
        result += i

    print('#{0} {1}'.format(tc, result))