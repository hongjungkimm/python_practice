def solution(n, s):
    answer = []
    a = s // n
    b = s % n
    
    if a:
        if b:
            answer = [a] * n
            cnt = b
            for i in range(n):
                answer[i] += 1
                cnt -= 1
                if cnt == 0:
                    break
            answer.sort()
            return answer
        else:
            return [a] * n
    else:
        return [-1]