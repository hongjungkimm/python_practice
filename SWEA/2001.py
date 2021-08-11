T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    puzzle = []
    for n in range(N):
        numbers = list(map(int, input().split()))
        puzzle.append(numbers)
    
    num_max = 0
    for line in puzzle[:M]:
        num_max += sum(line[:M])

    for i1 in range(N-M+1):
        for i2 in range(N-M+1):
            temp = 0
            for line in puzzle[i2:M+i2]:
                temp += sum(line[i1:M+i1])
            if temp > num_max:
                num_max = temp
    
    print(f'#{tc+1} {num_max}')
        