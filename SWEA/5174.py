def search_subtree(node):
    if sum(tree[node]) == 0:
        return 0
    return 1 + search_subtree(tree[node][1]) + search_subtree(tree[node][2])

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]

    for i in range(0, 2*(E-1)+1, 2):
        if tree[tmp[i]][1] == 0:
            tree[tmp[i]][1] = tmp[i+1]
            tree[tmp[i+1]][0] = tmp[i]
        else:
            tree[tmp[i]][2] = tmp[i+1]
            tree[tmp[i+1]][0] = tmp[i]

    print('#{0} {1}'.format(tc, search_subtree(N)))