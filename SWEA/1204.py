T = int(input())

for tc in range(T):
    tc_num = int(input())
    scores = list(map(int, input().split()))

    scores_2 = []
    for i in range(len(scores)):
        cnt = 0
        for e in range(len(scores)):
            if scores[i] == scores[e]:
                cnt += 1
        scores_2.append(cnt)
    
    scores_index = []
    num = max(scores_2)
    for i in range(len(scores_2)):
        if scores_2[i] == num:
            scores_index.append(i)
    
    result_scores = []
    for i in scores_index:
        result_scores.append(scores[i])
    
    result = max(result_scores)

    print(f'#{tc+1} {result}')
