T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [] # 이중배열 형태로 미로 만들어주기
    for _ in range(N):
        tmp = []
        for i in input():
            tmp.append(int(i))
        maze.append(tmp)

    di = [-1, 0, 0, 1] # 상 우 좌 하
    dj = [0, 1, -1, 0]

    ni = 0
    nj = 0
    for i in range(N): # 시작점 인덱스를 구하기 위한 반복문
        for j in range(N):
            if maze[i][j] == 2:
                ni = i
                nj = j
                break

    path = [[ni, nj]] # path(스택)에 시작점을 추가
    maze[ni][nj] = 4 # 시작점의 값을 4(이미 지나온 길을 의미)로 변환
    success = False # 미로 성공 여부
    while True:
        i, j = ni, nj # 현재 위치점에서 이동가능 여부를 파악하기 위한 변수
        for n in range(4): # '상 우 좌 하'를 현재 위치점에 더해주며 다음 이동 위치점 파악
            ni = i + di[n]
            nj = j + dj[n]
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1: # 다음 이동 위치점이 범위 안에 있고
                if maze[ni][nj] == 0: # 통로이면
                    path.append([ni, nj]) # path에 추가하고
                    maze[ni][nj] = 4 # 그 길은 4로 변환
                    break
                elif maze[ni][nj] == 3: # 도착점이면
                    path.append([ni, nj]) # path에 추가하고
                    success = True # 성공 여부 변환
                    break
        else: # '상 우 좌 하'를 다 더해준 다음 이동위치점이 이동 불가점이라면
            path.pop() # 현재 위치점을 path에서 제거하고
            if len(path) == 0: # 만약 현재 위치점을 제거한 path 경로가 더 이상 없다면 멈춤(실패)
                break
            ni = path[-1][0] # 그 전 위치점으로 인덱스 변환
            nj = path[-1][1]

        if success: # 성공이면 전체 반복문 멈춤
            break

    if success:
        print('#{0} 1'.format(tc))
    else:
        print('#{0} 0'.format(tc))