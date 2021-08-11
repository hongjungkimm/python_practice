T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = [] # 각 구간의 합 리스트
    for i in range(N-M+1):
        tmp = 0 # 각 구간의 합을 구하기 위한 임시 변수
        for j in numbers[i:i+M]: # 각 구간을 반복해서 지정 ex) [0:5] - [1:6] - [2:7] ~ ...
            tmp += j
        sum_list.append(tmp) # 각 구간의 합을 구간 합 리스트에 추가

    for i in range(len(sum_list)-1, 0, -1): # 버블 정렬로 합 리스트를 오름차순 정렬
        for j in range(i):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

    difference = sum_list[-1] - sum_list[0] # 합 리스트의 가장 큰 수와 가장 작은 수의 차이를 구함
    print('#{0} {1}'.format(tc, difference))