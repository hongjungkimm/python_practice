T = int(input())

for tc in range(1, T+1):
    money = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    check = [0] * 8

    for i in range(8):
        check[i] = money // won[i]
        money %= won[i]

    print('#{0}'.format(tc))
    print(*check)