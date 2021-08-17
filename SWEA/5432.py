T = int(input())

for tc in range(1, T+1):
    steels = input()

    cnt = 0
    current = 0
    for i in range(len(steels)):
        if steels[i] == '(':
            if steels[i+1] == ')':
                cnt += current
            else:
                current += 1
        else:
            if steels[i-1] == '(':
                pass
            else:
                current -= 1
                cnt += 1

    print('#{0} {1}'.format(tc, cnt))