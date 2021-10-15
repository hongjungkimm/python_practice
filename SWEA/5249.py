def MST():
    global keys, visited
    for _ in range(V+1):
        min_idx = -1
        min_val = float('inf')
        for i in range(V+1):
            if not visited[i] and keys[i] < min_val:
                min_idx = i
                min_val = keys[i]

        visited[min_idx] = True
        for j, w in adj_list[min_idx]:
            if not visited[j] and w < keys[j]:
                keys[j] = w


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    adj_list = [[] for _ in range(V+1)]
    for n1, n2, w in edges:
        adj_list[n1].append([n2, w])
        adj_list[n2].append([n1, w])

    keys = [float('inf') for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    keys[0] = 0
    MST()

    result = sum(keys)
    print('#{0} {1}'.format(tc, result))