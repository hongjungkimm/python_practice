for _ in range(1, 11):
    tc = int(input())
    strings = [input() for _ in range(100)]

    result = 1
    for string in strings:
        for i in range(100):
            for j in range(100):
                if string[i:i+j] == string[i:i+j][::-1]:
                    if len(string[i:i+j]) > result:
                        result = len(string[i:i+j])

    for i in range(100):
        tmp = ''
        for string in strings:
            tmp += string[i]
        for j in range(100):
            for k in range(100):
                if tmp[j:j+k] == tmp[j:j+k][::-1]:
                    if len(tmp[j:j+k]) > result:
                        result = len(tmp[j:j+k])

    print('#{0} {1}'.format(tc, result))