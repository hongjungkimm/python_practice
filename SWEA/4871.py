T = int(input())

def dfs(v, end):
    stack = []
    result = [] # 그래프 경로를 입력하기 위한 리스트

    stack.append(v) # 처음 노드를 stack에 push
    while stack: # stack이 비어있다면 반복문은 종료(더 이상 경로가 없다는 뜻)
        v = stack.pop() # 현재 노드를 pop
        visited[v] = 1 # 방문 체크
        result.append(v) # 그래프 경로에 노드 추가
        for w in range(1, V+1): # 해당 v의 그래프를 돌면서 간선으로 연결되어 있고 방문 체크를 하지 않은 노드 탐색
            if graph[v][w] == 1 and visited[w] == 0:
                stack.append(w) # 그러한 노드가 있다면 stack에 push

    if end in result: # 만약 그래프 경로에 끝점이 들어가 있다면(시작점과 끝점이 연결되어 있다면)
        return 1
    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드 수의 간선 수
    graph = [[0] * (V + 1) for _ in range(V + 1)] # 행렬 만들어 주기
    for _ in range(E):
        v, e = map(int, input().split()) # 각 노드의 연결된 간선을 받아서
        graph[v][e] = 1 # 행렬에 표기
    S, G = map(int, input().split()) # 시작점과 끝점
    visited = [0 for _ in range(V + 1)] # 방문 리스트 만들어 주기

    print('#{0} {1}'.format(tc, dfs(S, G)))
