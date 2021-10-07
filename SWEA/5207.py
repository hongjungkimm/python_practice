def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    flag = 'empty'
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            if flag == 'left':
                break
            right = mid - 1
            flag = 'left'
        elif arr[mid] < target:
            left = mid + 1
            if flag == 'right':
                break
            flag = 'right'

    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for num in B:
        cnt += binary_search(A, num)

    print('#{0} {1}'.format(tc, cnt))