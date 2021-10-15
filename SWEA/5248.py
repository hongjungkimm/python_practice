def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    papers = []
    for i in range(0, M*2, 2):
        papers.append([temp[i], temp[i+1]])

    ranks = [0 for _ in range(N+1)]
    parents = [0 for _ in range(N + 1)]
    for i in range(1, N+1):
        parents[i] = i

    for paper in papers:
        p0 = find_set(paper[0])
        p1 = find_set(paper[1])

        if ranks[p0] > ranks[p1]:
            parents[p1] = p0
        elif ranks[p0] < ranks[p1]:
            parents[p0] = p1
        else:
            parents[p0] = p1

    result = set()
    for i in range(1, N+1):
        result.add(find_set(parents[i]))
    print('#{0} {1}'.format(tc, len(result)))
