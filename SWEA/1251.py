def MST():
    global keys, visited

    for _ in range(N):
        min_idx = -1
        min_val = float('inf')
        for i in range(N):
            if not visited[i] and keys[i] < min_val:
                min_idx = i
                min_val = keys[i]

        visited[min_idx] = True
        for i in range(N):
            if i != min_idx:
                if not visited[i] and ((islands[i][0] - islands[min_idx][0]) ** 2 + (islands[i][1] - islands[min_idx][1]) ** 2) * E < keys[i]:
                    keys[i] = ((islands[i][0] - islands[min_idx][0]) ** 2 + (islands[i][1] - islands[min_idx][1]) ** 2) * E


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    islands = []
    for i in range(N):
        temp = [Y[i], X[i]]
        islands.append(temp)

    keys = [float('inf') for _ in range(N)]
    visited = [False for _ in range(N)]
    keys[0] = 0
    MST()
    print(keys)
    print('#{0} {1}'.format(tc, round(sum(keys))))
