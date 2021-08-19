T = int(input())

for tc in range(1, T+1):
    s = input()
    s_list = [s[i] for i in range(len(s))]

    stack = []
    for i in range(len(s_list)):
        if len(stack) == 0:
            stack.append(s_list[i])
        elif stack[-1] == s_list[i]:
            stack.pop()
        else:
            stack.append(s_list[i])

    result = len(stack)
    print('#{0} {1}'.format(tc, result))