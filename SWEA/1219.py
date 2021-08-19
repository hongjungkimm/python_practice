def dfs(v):
    stack = []
    result = [] # 최종 그래프 경로

    stack.append(v)
    while stack: # stack이 비어있으면 자동으로 반복문 종료(더 이상 경로가 없음)
        v = stack.pop()
        if visited[v] == 0: # 방문 체크가 되어 있지 않으면 방문 체크
            visited[v] = 1
            result.append(v) # 방문 했기에 최종 그래프 경로에 입력
        for w in range(100):
            if graph[v][w] == 1 and visited[w] == 0:
                stack.append(w) # 그래프에 해당 노드의 간선이 1이고 방문 체크가 되어있지 않다면 stack에 push
    if 99 in result: # 99(B)가 최종 그래프 경로에 있다면 1을 반환
        return 1
    else: # 아니면 0을 반환
        return 0

for tc in range(1, 11):
    T, n = map(int, input().split())
    tmp = list(map(int, input().split())) # 노드와 간선을 입력하기 위한 임시 리스트

    graph = [[0] * 100 for _ in range(100)] # 빈 행렬 생성
    for i in range(0, len(tmp)-1, 2):
        graph[tmp[i]][tmp[i+1]] = 1 # 노드와 간선을 행렬에 입력(단방향)
    visited = [0 for _ in range(100)] # 방문 체크를 위한 빈 리스트 생성

    print('#{0} {1}'.format(tc, dfs(0)))
