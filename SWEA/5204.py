def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    elif right_idx < len(right):
        result.extend(right[right_idx:])

    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    result_list = merge_sort(numbers)

    print('#{0} {1} {2}'.format(tc, result_list[len(numbers)//2], cnt))