import sys

N = int(sys.stdin.readline()) # 스위치의 개수
status = [0] + list(map(int, sys.stdin.readline().split())) # 인덱스 조작을 위해 앞에 [0]을 하나 추가!
S = int(sys.stdin.readline()) # 학생 수
switches = [list(map(int, sys.stdin.readline().split())) for _ in range(S)] # 학생들의 스위치 조작 리스트
# 남자는 [1, 3] 여자는 [2, 3]이고
# 남자는 부여받은 수의 배수의 상태를 바꿈! ex. 3이 주어지면 3과 6의 상태를 바꿈!
# 여자는 부여받은 수의 상태를 변화시킨 후 대칭을 한 칸씩 보면서 좌우가 대칭이면 상태를 바꾸고 아니면 바로 종료!

for switch in switches:
    if switch[0] == 1: # 만약 남자이면
        j = 1 # 배수를 만들어 주기 위한 변수
        while True:
            i = switch[1] # 남자가 부여받은 수
            i = i * j # ex. 3 * 1 --- 3 * 2 ---
            if i <= len(status) - 1:
                if status[i]:
                    status[i] = 0
                else:
                    status[i] = 1
            else: # 배수가 전체 스위치 길이를 벗어나면 종료
                break
            j += 1
    else: # 만약 여자이면
        i = 1
        while True:
            if switch[1] - i < 1 or len(status) - 1 < switch[1] + i: # 대칭을 보는 범위가 0 혹은 길이에 벗어나면 종료
                break
            if status[switch[1] - i] == status[switch[1] + i]: # 좌우 대칭 확인
                if status[switch[1] - i]: # 1이면
                    status[switch[1] - i] = status[switch[1] + i] = 0
                else: # 0이면
                    status[switch[1] - i] = status[switch[1] + i] = 1
            else: # 대칭이 아니면 바로 종료
                break
            i += 1
        if status[switch[1]]: # 여자가 부여받은 수의 상태변환
            status[switch[1]] = 0
        else:
            status[switch[1]] = 1


for i in range(len(status[1:])//20+1): # 20개씩 출력하므로
    print(' '.join(list(map(str, status[1:][i * 20:i * 20 + 20]))))