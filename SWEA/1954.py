T = int(input())

for tc in range(1, T+1):
    N = int(input())
    puzzle = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    n = 1
    d = 0 # 0 = 오른쪽, 1 = 아래, 2 = 왼쪽, 3 = 위
    i, j = 0, -1
    while n <= N ** 2:
        ni, nj = i + di[d], j + dj[d]
        if ni < len(puzzle) and nj < len(puzzle) and puzzle[ni][nj] == 0:
            puzzle[ni][nj] = n
            n += 1
            i, j = ni, nj
        else:
            d = (d + 1) % 4

    print('#{0}'.format(tc))
    for i in puzzle:
        print(' '.join(list(map(str, i))))