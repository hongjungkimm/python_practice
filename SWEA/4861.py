T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    strings = [input() for _ in range(N)]

    result = ''
    for string in strings:
        for i in range(N - M + 1):
            if string[i:i+M] == string[i:i+M][::-1]:
                result = string[i:i+M]

    for i in range(N):
        tmp = ''
        for string in strings:
            tmp += string[i]
        for j in range(N - M + 1):
            if tmp[j:j+M] == tmp[j:j+M][::-1]:
                result = tmp[j:j+M]

    print('#{0} {1}'.format(tc, result))