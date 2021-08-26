def bfs(s, g): # 함수에서는 바로 리턴을 때려라!! flag 다 지우고 다시 제출
    queue = []
    visited = [0 for _ in range(V + 1)]

    queue.append(s)
    flag = False
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
        for w in range(V + 1):
            if graph[v][w] == 1 and not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1
                if w == g:
                    flag = True
                    break
        if flag:
            break
    if visited[g] == 0:
        return 0
    return visited[g] - visited[s]

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for i in tmp:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    print('#{0} {1}'.format(tc, bfs(S, G)))