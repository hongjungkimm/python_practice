T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    squares = [list(map(int, input().split())) for _ in range(N)]

    puzzle = [[0] * 10 for _ in range(10)] # 0으로 이루어지 좌표
    for s in squares: # squares의 요소를 하나씩 반복해서 불러옴 ex) [2, 2, 4, 4, 1]
        for i in range(s[0], s[2] + 1): # y축을 2 ~ 4까지
            for j in range(s[1], s[3] + 1): # x축을 2 ~ 4까지
                puzzle[i][j] += s[4] # 해당 색으로 칠해줌

    purple = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 3: # 보라색은 빨강(1), 파랑(2)이 합쳐진 3이므로
                purple += 1

    print('#{0} {1}'.format(tc, purple))