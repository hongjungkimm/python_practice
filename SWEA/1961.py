T = int(input())

def rotate_puzzle(list1, n):
    puzzle = []
    for i in range(n):
        temp = []
        for e in list1[::-1]:
            temp.append(str(e[i]))
        puzzle.append(temp)
    return puzzle

for tc in range(T):
    N = int(input())
    puzzle_0 = []
    for n in range(N):
        numbers = list(map(int, input().split()))
        puzzle_0.append(numbers)
    puzzle_90 = rotate_puzzle(puzzle_0, N)
    puzzle_180 = rotate_puzzle(puzzle_90, N)
    puzzle_270 = rotate_puzzle(puzzle_180, N)
    
    print(f'#{tc+1}')
    for n in range(N):
        print(''.join(puzzle_90[n]), ''.join(puzzle_180[n]), ''.join(puzzle_270[n]))