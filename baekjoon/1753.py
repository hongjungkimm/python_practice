import sys
import heapq
from collections import defaultdict

def dijkstra(start):
    global key

    queue = []
    heapq.heappush(queue, (0, start))
    key[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if key[now] < dist:
            continue

        for node in adj_list[now]:
            if dist + node[1] < key[node[0]]:
                key[node[0]] = dist + node[1]
                heapq.heappush(queue, (dist + node[1], node[0]))


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

adj_list = defaultdict(list)
key = [float('inf') for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    adj_list[s].append((e, w))

dijkstra(start)

for i in range(1, V+1):
    if key[i] == float('inf'):
        print('INF')
    else:
        print(key[i])