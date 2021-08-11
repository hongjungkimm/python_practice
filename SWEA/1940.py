T = int(input())

for tc in range(T):
    distance, velocity = 0, 0
    N = int(input())

    for i in range(N):
        tmp = list(map(int,input().split()))

        if tmp[0] == 1:
            velocity += tmp[1]
        elif tmp[0] == 2:
            velocity = max(0, velocity-tmp[1])

        distance += velocity

    print(f'#{tc+1} {distance}')
        