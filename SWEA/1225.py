for _ in range(1, 11):
    tc = int(input())
    numbers = list(map(int, input().split()))
    flag = False
    while True:
        for i in range(1, 6):
            numbers.append(numbers[0] - i)
            numbers.pop(0)
            if numbers[-1] <= 0:
                flag = True
                break
        if flag:
            break
    numbers[-1] = 0
    print('#{0} {1}'.format(tc, ' '.join(list(map(str, numbers)))))