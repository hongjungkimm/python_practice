def find_min(array, n, h):
    global result
    if n > result:
        return
    if h == N:
        result = min(result, n)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min(array, n+array[h][i], h+1)
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    visited = [0] * N
    find_min(array, 0, 0)

    print('#{0} {1}'.format(tc, result))