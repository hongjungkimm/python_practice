T = int(input())

for tc in range(T):
    puzzle = []
    for i in range(9):
        line = list(map(int, input().split()))
        puzzle.append(line)
    
    answer = 1
    for puzzle_width in puzzle:
        puzzle_width_sort = sorted(puzzle_width)
        if puzzle_width_sort != list(range(1, 10)):
            answer = 0
    
    puzzle_vertical = []
    for i in range(9):
        temp = []
        for puzzle_height in puzzle:
            temp.append(puzzle_height[i])
        puzzle_vertical.append(temp)
    
    for vertical in puzzle_vertical:
        vertical_sort = sorted(vertical)
        if vertical_sort != list(range(1, 10)):
            answer = 0
    
    puzzle_square = []
    i = [0, 1, 2]
    for a in i:    
        for b in i:
            for c in i:
                temp = []
                for line in puzzle[c*3:(c+1)*3]:
                    for n in line[b*3:(b+1)*3]:
                        temp.append(n)
                puzzle_square.append(temp)
    
    for square in puzzle_square:
        square_sort = sorted(square)
        if square_sort != list(range(1, 10)):
            answer = 0
    
    print(f'#{tc+1} {answer}')
                