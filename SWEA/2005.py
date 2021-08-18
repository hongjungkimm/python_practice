T = int(input())

for tc in range(1, T+1):
    cnt = int(input())
    triangle = [[1]]
    for i in range(cnt-1):
        tmp = [1]
        for j in range(len(triangle[i])-1):
            tmp.append(triangle[i][j] + triangle[i][j+1])
        tmp.append(1)
        triangle.append(tmp)

    print('#{0}'.format(tc))
    for line in triangle:
        print(' '.join(map(str, line)))