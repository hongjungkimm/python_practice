import sys

def min_difference(idx, total):
    global difference
    if total == target:
        difference = 0
        return
    elif total > target:
        if difference > total - target:
            difference = total - target

    for i in range(idx+1, N):
        min_difference(i, total + height[i])

T = int(input())

for tc in range(1, T+1):
    N, target = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort(reverse=True)

    difference = float('inf')
    for i in range(N):
        min_difference(i, height[i])
        if difference == 0:
            break

    print('#{0} {1}'.format(tc, difference))