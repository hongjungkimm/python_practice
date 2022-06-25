def solution(n, money):
    def bfs(now, num):
        nonlocal remainder, answer, length

        if num == 0:
            answer += 1
            return
        
        if remainder[-1] == 0:
            return
        
        for i in range(now, length):
            if remainder[i] > 0 and num - money[i] >= 0:
                remainder[i] -= 1
                bfs(i, num - money[i])
                remainder[i] += 1
    
    money.sort(reverse=True)
    remainder = []
    for i in money:
        remainder.append(n // i)
    
    answer = 0
    length = len(money)
    bfs(0, n)
    return answer

print(solution(5, [1, 2, 5]))