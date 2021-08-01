import sys # 나중에 heapq 모듈로 다시 풀어보기, 일단은 시간초과로 실패

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    command = int(sys.stdin.readline())
    if command > 0:
        numbers.append(command)
        numbers.sort()
    else:
        if numbers:
            print(numbers[0])
            numbers = numbers[1:]
        else:
            print(0)