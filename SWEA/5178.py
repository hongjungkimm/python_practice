T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(M)]
    tree = [[0] * 2 for _ in range(N+1)]

    for node in nodes:
        tree[node[0]][1] = node[1] # 리프노드 표시
        tree[node[0]][0] = node[0] // 2 # 각 리프노드의 부모노드 표시

    for node in tree[::-1]:
        tree[node[0]][1] += node[1]
        tree[node[0]][0] = node[0] // 2

    print('#{0} {1}'.format(tc, tree[L][1]))