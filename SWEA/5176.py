def make_tree(node):
    if node == 0:
        return ''
    return make_tree(tree[node][1]) + ' ' + str(node) + ' ' + make_tree(tree[node][2])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]

    for i in range(1, N//2+1):
        if 2*i <= N:
            tree[i][1] = 2*i
            tree[2*i][0] = i
        if 2*i+1 <= N:
            tree[i][2] = 2*i+1
            tree[2*i+1][0] = i

    result = make_tree(1)
    result = [0] + list(map(int, result[1:-1].split()))
    a = 0
    b = 0
    for i in range(1, N+1):
        if result[i] == 1:
            a = i
        if result[i] == N // 2:
            b = i
    print('#{0} {1} {2}'.format(tc, a, b))