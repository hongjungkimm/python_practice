from collections import defaultdict

def solution(n, s, a, b, fares):
    def search_shortest(start, end, distance, trace):
        nonlocal adj_list, visited, min_distance, trace_list
        if distance > min_distance:
            return
        
        if start == end:
            min_distance = distance
            trace_list = trace
        
        for i in adj_list[start]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                search_shortest(i[0], end, distance + i[1], trace + [i[0]])
                visited[i[0]] = False
    
    adj_list = defaultdict(list)
    for fare in fares:
        adj_list[fare[0]].append([fare[1], fare[2]])
        adj_list[fare[1]].append([fare[0], fare[2]])
    
    visited = [False] * (n + 1)
    min_distance = float('inf')
    trace_list = []
    visited[s] = True
    search_shortest(s, a, 0, [])
    trace_a = trace_list[:]
    min_a = min_distance

    visited = [False] * (n + 1)
    min_distance = float('inf')
    trace_list = []
    visited[s] = True
    search_shortest(s, b, 0, [])
    trace_b = trace_list[:]
    min_b = min_distance

    answer = 0
    return trace_a, min_a, trace_b, min_b

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))