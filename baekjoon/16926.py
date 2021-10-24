import sys

def rotate(array):
    result = [[0] * M for _ in range(N)]

    start = 0
    minus = 0
    while True:
        i = j = start
        for _ in range(N-1-minus):
            result[i+1][j] = array[i][j]
            i += 1
        
        for _ in range(M-1-minus):
            result[i][j+1] = array[i][j]
            j += 1
        
        for _ in range(N-1-minus):
            result[i-1][j] = array[i][j]
            i -= 1
        
        for _ in range(M-1-minus):
            result[i][j-1] = array[i][j]
            j -= 1
        
        if result[i+1][j+1] == 0:
            start += 1
            minus += 2
        else:
            return result


N, M, R = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(R):
    array = rotate(array)

for a in array:
    print(*a)