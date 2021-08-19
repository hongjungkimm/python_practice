for tc in range(1, 11):
    n, numbers = map(str, input().split())

    stack = []
    for i in range(int(n)):
        if len(stack) == 0:
            stack.append(numbers[i])
        elif numbers[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(numbers[i])

    print('#{0} {1}'.format(tc, ''.join(stack)))
