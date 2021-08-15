import sys

N = int(sys.stdin.readline())
status = [0] + list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())
switches = [list(map(int, sys.stdin.readline().split())) for _ in range(S)]

for switch in switches:
    if switch[0] == 1:
        j = 1
        while True:
            i = switch[1]
            i = i * j
            if i <= len(status) - 1:
                if status[i]:
                    status[i] = 0
                else:
                    status[i] = 1
            else:
                break
            j += 1
    else:
        i = 1
        while True:
            if switch[1] - i < 1 or len(status) - 1 < switch[1] + i:
                break
            if status[switch[1] - i] == status[switch[1] + i]:
                if status[switch[1] - i]:
                    status[switch[1] - i] = status[switch[1] + i] = 0
                else:
                    status[switch[1] - i] = status[switch[1] + i] = 1
            else:
                break
            i += 1
        if status[switch[1]]:
            status[switch[1]] = 0
        else:
            status[switch[1]] = 1


for i in range(len(status[1:])//20+1):
    print(' '.join(list(map(str, status[1:][i * 20:i * 20 + 20]))))