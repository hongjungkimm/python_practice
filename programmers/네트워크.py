def solution(n, computers):
    def find_root(num):
        nonlocal root

        if num == root[num]:
            return num

        return find_root(root[num])
        

    root = list(range(n))
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and computers[j][i] == 1:
                a = find_root(i)
                b = find_root(j)
                if a > b:
                    root[a] = b
                else:
                    root[b] = a
    
    answer_list = []
    for i in range(n):
        answer_list.append(find_root(i))
    
    answer = len(set(answer_list))
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))