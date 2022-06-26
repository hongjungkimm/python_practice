import sys
from tracemalloc import start

N = int(sys.stdin.readline())
targets = [i for i in list(map(int, sys.stdin.readline().split()))]
M = int(sys.stdin.readline())
nums = [i for i in list(map(int, sys.stdin.readline().split()))]

targets.sort()

for n in nums:
    flag = False
    start = 0
    end = len(targets) - 1
    mid = (start + end) // 2
    while start <= end:
        if targets[mid] < n:
            start = mid + 1
            mid = (start + end) // 2
        elif targets[mid] > n:
            end = mid - 1
            mid = (start + end) // 2
        else:
            flag = True
            break
    if flag:
        print(1)
    else:
        print(0)
