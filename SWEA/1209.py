for tc in range(10):
    T = int(input())
    puzzle = []
    for _ in range(100):
        line = list(map(int, input().split()))
        puzzle.append(line)

    result = 0
    for line in puzzle:
        tmp = 0
        for i in range(100):
            tmp += line[i]
        if tmp > result:
            result = tmp

    for i in range(100):
        tmp = 0
        for line in puzzle:
            tmp += line[i]
        if tmp > result:
            result = tmp

    tmp1 = 0
    tmp2 = 0
    for i in range(100):
        tmp1 += puzzle[i][i]
        tmp2 += puzzle[i][99-i]
    if tmp1 > result and tmp2 > result:
        if tmp1 > tmp2:
            result = tmp1
        else:
            result = tmp2
    
    print(f'#{T} {result}')

