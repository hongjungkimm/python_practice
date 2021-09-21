import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
check = [0 for _ in range(N)]

check[N-1] = 1
if stairs[0] <= stairs[1]:
    check[1] = 1
    i = 1
else:
    check[0] = 1
    i = 0
while True:
    if i < 2:
        if stairs[i+1] >= stairs[i+2]:
            check[i+1] = 1
            i += 1
            if i >= N-2:
                break
        else:
            check[i+2] = 1
            i += 2
            if i >= N-2:
                break
    else:
        if check[i-1] == 1:
            check[i+2] = 1
            i += 2
            if i >= N-2:
                break
        else:
            if stairs[i+1] >= stairs[i+2]:
                check[i+1] = 1
                i += 1
                if i >= N-2:
                    break
            else:
                check[i+2] = 1
                i += 2
                if i >= N-2:
                    break


if sum(check[:3]) < 2:
    check[0] = 1

result = 0
for i in range(N):
    if check[i] == 1:
        result += stairs[i]

print(result)