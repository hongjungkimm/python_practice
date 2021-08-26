T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    seconds = list(map(int, input().split()))

    seconds.sort() # 도착시간을 오름차순으로 정렬
    bread = 0
    time = 0
    i = 0
    flag = False
    while i < N:
        time += M # 시간을 M만큼 증가
        bread += K # 빵의 개수를 K만큼 증가
        if seconds: # 도착한 사람이 있고
            j = 0
            while bread and seconds:
                if time > seconds[j]:
                    flag = True
                    break
                seconds.pop(0)
                bread -= 1
        else:
            break
        if flag:
            break
        i += 1

    if seconds:
        result = 'Impossible'
    else:
        result = 'Possible'
    print('#{0} {1}'.format(tc, result))