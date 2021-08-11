T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    cmd_box = [0] * (Q + 1) # 각 줄의 명령을 저장하는 리스트를 생성
    for i in range(1, Q+1):
        command = list(map(int, input().split()))
        cmd_box[i] = command # cmd_box[[L, R], [1, 3], [2, 4] ....]

    num_box = [0] * (N + 1) # 숫자를 넣을 빈 박스 리스트를 생성
    for i in range(1, Q+1): # 명령줄의 수 만큼 반복
        for j in range(cmd_box[i][0], cmd_box[i][1]+1): # 각 줄의 L, R+1을 범위로 설정
            num_box[j] = i

    num_box = [str(i) for i in num_box[1:]] # join을 하기 위해 num_box의 요소를 string으로 변경
    print('#{0} {1}'.format(tc, ' '.join(num_box)))