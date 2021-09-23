def make_tree(i, n):
    tree[i] = n
    parent_idx = i // 2

    while i != 1 and tree[parent_idx] > tree[i]:
        tree[parent_idx], tree[i] = tree[i], tree[parent_idx]
        i = parent_idx
        parent_idx = parent_idx // 2


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    tree = [0] * (N+1)

    idx = 0
    for num in numbers:
        idx += 1
        make_tree(idx, num)

    result = 0
    i = N // 2
    while i:
        result += tree[i]
        i //= 2
    print('#{0} {1}'.format(tc, result))