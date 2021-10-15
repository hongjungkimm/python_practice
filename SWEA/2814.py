T = int(input())

def dfs(start, d):
    global visited
    global result
    if d > result:
        result = d

    for i in adj_list[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, d+1)
            visited[i] = 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    adj_list = [[] for _ in range(N+1)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    result = 0
    for start in range(1, N+1):
        visited = [0] * (N + 1)
        visited[start] = 1
        dfs(start, 1)

    print('#{0} {1}'.format(tc, result))