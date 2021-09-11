import sys
import heapq

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
heap = []
for n in numbers:
    if n == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)