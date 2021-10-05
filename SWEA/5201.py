T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    trucks_check = [0] * M

    i = 0
    for container in containers:
        if trucks[i] >= container:
            trucks_check[i] = container
            i += 1
            if i > M-1:
                break

    print('#{0} {1}'.format(tc, sum(trucks_check)))