T = int(input())

for tc in range(1, T+1):
    N, M  = map(int, input().split())
    codes = [[i for i in input()] for _ in range(N)]
    code_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
                 '0101111':6, '0111011': 7, '0110111': 8, '0001011': 9}

    ki = 0
    kj = 0
    for i in range(N):
        for j in range(M):
            if ''.join(codes[i][::-1][j:j+7][::-1]) in code_dict.keys():
                ki = i
                kj = j
                break

    final_code = codes[ki][::-1][kj:kj+56][::-1]
    num_code = [0]
    for i in range(8):
        num_code.append(code_dict[''.join(final_code[i*7:i*7+7])])

    result = (int(num_code[1]) + int(num_code[3]) + int(num_code[5]) + int(num_code[7])) * 3 + int(num_code[2]) + int(num_code[4]) + int(num_code[6]) + int(num_code[8])
    if result % 10:
        print('#{0} 0'.format(tc))
    else:
        print('#{0} {1}'.format(tc, sum(map(int, num_code))))