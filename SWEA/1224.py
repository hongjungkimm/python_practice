for tc in range(1, 11):
    N = int(input())
    cal = input()

    chg_cal = []
    stack = []
    for i in range(N):
        if cal[i].isdigit():
            chg_cal.append(int(cal[i]))
        else:
            stack.append(cal[i])
            if len(stack) <= 1:
                continue
            while True:
                if len(stack) == 0:
                    break
                if stack[-1] == '(':
                    break
                elif stack[-2] == '(':
                    break
                elif stack[-1] == ')':
                    stack.pop()
                    while stack[-1] != '(':
                        chg_cal.append(stack.pop())
                    stack.pop()
                elif stack[-1] == stack[-2]:
                    chg_cal.append(stack.pop())
                elif stack[-2] == '+' and stack[-1] == '*':
                    break
                elif stack[-2] == '*' and stack[-1] == '+':
                    chg_cal.append(stack.pop(-2))
    while stack:
        chg_cal.append(stack.pop())

    result = []
    for i in range(len(chg_cal)):
        if type(chg_cal[i]) == int:
            result.append(chg_cal[i])
        else:
            if chg_cal[i] == '+':
                n1 = result.pop()
                n2 = result.pop()
                result.append(n2+n1)
            else:
                n1 = result.pop()
                n2 = result.pop()
                result.append(n2*n1)

    print('#{0} {1}'.format(tc, result[0]))