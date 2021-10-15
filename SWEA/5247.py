from collections import deque

def operation(N, M):
    global result, visited
    queue = deque([[N, 0]])

    while queue:
        num, cnt = queue.popleft()
        if num == M:
            result = cnt
            return
        if 0 < num + 1 <= 1000000 and not visited[num+1]:
            queue.append([num + 1, cnt + 1])
            visited[num+1] = True
        if 0 < num - 1 <= 1000000 and not visited[num-1]:
            queue.append([num - 1, cnt + 1])
            visited[num - 1] = True
        if 0 < num * 2 <= 1000000 and not visited[num*2]:
            queue.append([num * 2, cnt + 1])
            visited[num * 2] = True
        if 0 < num - 10 <= 1000000 and not visited[num-10]:
            queue.append([num - 10, cnt + 1])
            visited[num - 10] = True

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = 0
    visited = [False] * 1000001
    visited[N] = True
    operation(N, M)
    print('#{0} {1}'.format(tc, result))