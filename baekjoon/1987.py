import sys

def bfs(board, R, C):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    answer = 0
    queue = set([(0, 0, board[0][0])])
    
    while queue:
        x, y, trace = queue.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in trace:
                queue.add((ni, nj, trace + board[ni][nj]))
        if len(trace) > answer:
            answer = len(trace)
    
    return answer
                    

R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    temp = []
    str1 = sys.stdin.readline().rstrip()
    for s in str1:
        temp.append(s)
    board.append(temp)

print(bfs(board, R, C))