def change_binary(num):
    result = ''
    i = 0
    while True:
        num *= 2
        i += 1
        if num >= 1:
            result += '1'
            num -= 1
            if num == 0:
                break
        else:
            result += '0'
        if num >= 1:
            break
        if i > 12:
            return 'overflow'

    return result

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    print('#{0} {1}'.format(tc, change_binary(N)))