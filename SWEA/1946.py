T = int(input())

for tc in range(T):
    N = int(input())
    result = ''
    for n in range(N):
        alpha, number = input().split()
        number = int(number)
        alnum = alpha * number
        result += alnum
    print(f'#{tc+1}')
    if len(result) % 10:
        for i in range(len(result)//10):
            print(result[i * 10:(i+1) * 10])
        print(result[len(result) - (len(result) % 10):])
    else:
        for i in range(len(result)//10):
            print(result[i * 10:(i+1) * 10])

