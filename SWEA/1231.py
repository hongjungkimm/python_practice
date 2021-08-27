def inorder(node):
    if node != 0:
        inorder(int(tree[node][2]))
        print(tree[node][1], end="")
        inorder(int(tree[node][3]))

for tc in range(1, 11):
    N = int(input())
    tree = [list(map(str, input().split())) for _ in range(N)]
    for i in tree:
        if len(i) < 4:
            i += ['0'] * (4 - len(i))
    tree = [['0', '0', '0', '0']] + tree

    print('#{0}'.format(tc), end=" ")
    inorder(1)
    print()