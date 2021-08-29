T = int(input())

for tc in range(T):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    
    answer = 1 # 검증을 위한 변수, 성공은 '1', 실패는 '0'
    for puzzle_width in puzzle: # 가로 검증
        puzzle_width_sort = sorted(puzzle_width)
        if puzzle_width_sort != list(range(1, 10)): # 정렬한 가로 줄이 1부터 9까지가 아니면 실패!
            answer = 0

    # 세로 줄을 리스트화
    puzzle_vertical = [] # 서로 줄을 만들어 넣기 위한 리스트
    for i in range(9):
        temp = []
        for puzzle_height in puzzle:
            temp.append(puzzle_height[i])
        puzzle_vertical.append(temp)
    
    for vertical in puzzle_vertical: # 세로 검증
        vertical_sort = sorted(vertical)
        if vertical_sort != list(range(1, 10)):
            answer = 0
    
    # 사각형을 리스트화
    puzzle_square = []
    term = [0, 1, 2]
    for i in term:
        for j in term:
            tmp = []
            for line in puzzle[i*3:i*3+3]:
                for vertical in line[j*3:j*3+3]:
                    tmp.append(vertical)
        puzzle_square.append(tmp)

    for square in puzzle_square: # 사각형 검증
        square_sort = sorted(square)
        if square_sort != list(range(1, 10)):
            answer = 0           
            
    print(f'#{tc+1} {answer}')
                