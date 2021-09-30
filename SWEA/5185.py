def change_binary(num):
    temp = ''
    if num == 1:
        temp = '1000'
    elif num == 0:
        temp = '0000'
    else:
        while True:
            temp += str(num % 2)
            num //= 2
            if num == 1:
                temp += str(num)
                break

        while len(temp) < 4:
            temp += '0'

    return temp[::-1]

T = int(input())

for tc in range(1, T+1):
    N, number = input().split()
    N = int(N)
    x_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

    result = ''
    for n in number:
        if n.isdigit():
            result += change_binary(int(n))
        else:
            result += change_binary(int(x_dict[n]))

    print('#{0} {1}'.format(tc, result))