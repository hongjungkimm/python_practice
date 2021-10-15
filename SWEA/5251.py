def dijkstra(s):
    distance[s] = 0

    for _ in range(N+1):

        min_idx = -1
        min_val = float('inf')
        for i in range(N+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1

        for i in range(N+1):
            if mat[min_idx][i] and not visited[i]:
                if distance[min_idx] + mat[min_idx][i] < distance[i]:
                    distance[i] = distance[min_idx] + mat[min_idx][i]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e, w in edges:
        mat[s][e] = w

    distance = [float('inf') for _ in range(N+1)]
    visited = [0] * (N + 1)

    start = 0
    dijkstra(start)

    print(f'#{tc} {distance[N]}')