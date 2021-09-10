import sys # 다시 풀어야 함
from pprint import pprint

N, M = map(int, sys.stdin.readline().split())

board = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]

result = []
for j in range(M - 7):
    for i in range(N - 7):
        tmp = 0
        for b in board[i:i+8]:
            tmp += abs(b[j:j+8].count('B') - 4)
        result.append(tmp)

pprint(board)