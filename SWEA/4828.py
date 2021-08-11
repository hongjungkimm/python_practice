T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)-1, 0, -1): # 버블정렬로 numbers 리스트를 오름차순 정렬
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = numbers[-1] - numbers[0] # 오름차순 정렬된 numbers 리스트의 가장 끝의 수(큰 수)와 가장 앞의 수(작은 수)의 차이

    print('#{0} {1}'.format(tc, result))