T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input().split()

    divide = []
    if N % 2:
        divide.append(cards[:N//2+1])
        divide.append(cards[N//2+1:])
    else:
        divide.append(cards[:N//2])
        divide.append(cards[N//2:])

    shuffle = []
    if N % 2:
        for i in range(len(divide[1])):
            shuffle.append(divide[0][i])
            shuffle.append(divide[1][i])
        shuffle.append(divide[0][-1])
    else:
        for i in range(len(divide[1])):
            shuffle.append(divide[0][i])
            shuffle.append(divide[1][i])

    print('#{0} {1}'.format(tc, ' '.join(shuffle)))
