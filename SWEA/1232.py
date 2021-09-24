def inorder(n):
    if len(nodes[n]) == 3:
        left = inorder(nodes[n][1])
        right = inorder(nodes[n][2])
        if nodes[n][0] == '+':
            return left + right
        elif nodes[n][0] == '-':
            return left - right
        elif nodes[n][0] == '*':
            return left * right
        else:
            return left / right
    else:
        return nodes[n][0]

for tc in range(1, 11):
    N = int(input())

    nodes = [[] for _ in range(N+1)]
    for _ in range(N):
        tmp = input().split()
        if len(tmp) == 4:
            nodes[int(tmp[0])].append(tmp[1])
            nodes[int(tmp[0])].append(int(tmp[2]))
            nodes[int(tmp[0])].append(int(tmp[3]))
        else:
            nodes[int(tmp[0])].append(int(tmp[1]))

    print('#{0} {1}'.format(tc, int(inorder(1))))