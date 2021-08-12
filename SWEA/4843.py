T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    i = 0 # 초기값
    while i < len(numbers)-1: # i가 인덱스의 끝이 되면 반복문 종료
        max_idx = i # 현 위치부터 시작해서 최대값의 인덱스 초기값
        for n in range(i+1, len(numbers)): # 항상 i 다음부터를 범위로 설정
            if numbers[n] > numbers[max_idx]:
                max_idx = n
        numbers[max_idx], numbers[i] = numbers[i], numbers[max_idx] # 가장 큰 수를 i 위치로 변경
        i += 1 # 다음 바꿔줄 인덱스로 이동

        min_idx = i # 현 위치부터 시작해서 최소값의 인덱스 초기값
        for n in range(i+1, len(numbers)): # 항상 i 다음부터를 범위로 설정
            if numbers[min_idx] > numbers[n]:
                min_idx = n
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx] # 가장 작은 수를 i 위치로 변경
        i += 1 # 다음 바꿔줄 인덱스로 이동

    print('#{0} {1}'.format(tc, ' '.join(list(map(str, numbers[:10])))))
