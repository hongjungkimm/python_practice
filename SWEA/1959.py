T = int(input())

for tc in range(T):
    n_A, n_B = list(map(int, input().split()))
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    min_j = []
    max_j = []
    if len(Aj) > len(Bj):
        min_j, max_j= Bj, Aj
    else:
        min_j, max_j = Aj, Bj
    
    result = []
    for i in range(len(max_j) - len(min_j) + 1):
        sum_j = 0
        h = 0
        for e in range(i, len(min_j) + i):
            sum_j += min_j[h] * max_j[e]
            h += 1
        result.append(sum_j)
    
    print(f'#{tc+1} {max(result)}')