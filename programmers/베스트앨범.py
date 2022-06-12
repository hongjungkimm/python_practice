from collections import defaultdict

def solution(genres, plays):
    genres_idx = defaultdict(list)
    genres_cnt = defaultdict(int)

    for i in range(len(genres)):
        genres_idx[genres[i]].append(i)
        genres_cnt[genres[i]] += plays[i]
    
    genres_cnt_list = list(genres_cnt.values())
    genres_cnt_list.sort(reverse=True)
    
    answer = []
    for i in genres_cnt_list:
        for genre in genres_cnt.keys():
            if genres_cnt[genre] == i:
                if len(genres_idx[genre]) == 1:
                    answer.append(genres_idx[genre][0])
                else:
                    genres_idx[genre].sort()
                    for _ in range(2):
                        tmp_max = 0
                        tmp_idx = 0
                        for j in genres_idx[genre]:
                            if j not in answer and plays[j] > tmp_max:
                                tmp_max = plays[j]
                                tmp_idx = j
                        answer.append(tmp_idx)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))