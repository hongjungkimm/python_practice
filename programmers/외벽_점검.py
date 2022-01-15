from collections import defaultdict

def solution(n, weak, dist):
    linked_list = defaultdict(list)
    for i in range(n):
        if i == n - 1:
            linked_list[i].append(0)
            linked_list[i].append(False)
        else:
            linked_list[i].append(i + 1)
            linked_list[i].append(False)
    
    answer = 0
    return linked_list

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))