import sys

chess1 = []
chess2 = []
for i in range(8):
    if i % 2:
        tmp1 = []
        tmp2 = []
        for j in range(8):
            if j % 2:
                tmp1.append('W')
                tmp2.append('B')
            else:
                tmp1.append('B')
                tmp2.append('W')
        chess1.append(tmp1)
        chess2.append(tmp2)
    else:
        tmp1 = []
        tmp2 = []
        for j in range(8):
            if j % 2:
                tmp1.append('B')
                tmp2.append('W')
            else:
                tmp1.append('W')
                tmp2.append('B')
        chess1.append(tmp1)
        chess2.append(tmp2)

N, M = map(int, sys.stdin.readline().split())
board = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]

result = []
for j in range(M - 7):
    for i in range(N - 7):
        tmp = []
        for b in board[i:i+8]:
            tmp.append(b[j:j+8])

        cnt_1 = 0
        for ti in range(8):
            for tj in range(8):
                if tmp[ti][tj] != chess1[ti][tj]:
                    cnt_1 += 1
        
        cnt_2 = 0
        for ti in range(8):
            for tj in range(8):
                if tmp[ti][tj] != chess2[ti][tj]:
                    cnt_2 += 1

        result.append(min(cnt_1, cnt_2))

print(min(result))