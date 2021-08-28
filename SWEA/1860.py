T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N명의 사람, M초에 K의 붕어빵
    seconds = list(map(int, input().split())) # N명의 도착시간 리스트(도착하자 바로 붕어빵 줘야 함, 웨이팅 있으면 안 됨)
    # 아하! 그러면 도착하는 시간에 맞춰서 바로 붕어빵이 완성되거나, 이미 붕어빵이 만들어져 있어야 하는구나!
    seconds.sort() # 도착시간을 오름차순으로 정렬
    bread = 0 # 만들어져 있는 빵의 개수를 세자!
    time = 0 # 붕어빵을 만든 시간을 체크하자!
    i = 0 # 사람의 수 만큼만 반복하자!
    flag = False
    while i < N:
        time += M # 시간을 M만큼 증가
        bread += K # 빵의 개수를 K만큼 증가
        # ex) 2초 후에 2개의 빵이 만들어져 있다!
        if seconds: # 도착한 사람이 있고
            j = 0
            while bread and seconds:
                if time > seconds[j]: # 예를 들어 3초에 빵을 만들었는데 2초에 사람이 오면 받지 못하니까 이 경우는 아예 실패!
                    flag = True
                    break
                seconds.pop(0) # 만약 빵을 받으면 받은 사람은 귀가시키고(ex. 2초에 2개의 빵이 있는데, 손님이 4초 6초에 올 예정이면 줄 수 있다고 생각하고 손님 리스트에서 제거하기!)
                bread -= 1 # 빵의 개수를 1개 줄이자!
        else: # 만약에 사람이 없으면 빵을 다 받았구나!
            break
        if flag:
            break
        i += 1

    if seconds:
        result = 'Impossible'
    else:
        result = 'Possible'
    print('#{0} {1}'.format(tc, result))