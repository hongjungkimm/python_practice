import sys
import heapq

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

heap = []
for n in numbers:
    if n:
        heapq.heappush(heap, (abs(n), n))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)