def quick_sort(arr, start, end):
    if start < end:
        pivot = arr[end]
        left = start
        right = end - 1

        while left < right:
            while arr[left] <= pivot:
                left += 1
                if left > right:
                    break

            while arr[right] >= pivot:
                right -= 1
                if left > right:
                    break

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]

        if arr[left] >= arr[end]:
            arr[left], arr[end] = arr[end], arr[left]

        quick_sort(arr, start, left - 1)
        quick_sort(arr, left + 1, end)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, N-1)
    print('#{0} {1}'.format(tc, numbers[N//2]))