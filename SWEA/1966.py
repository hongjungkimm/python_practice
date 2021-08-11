T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers_sort = sorted(numbers)
    numbers_sort = list(map(str, numbers_sort))
    numbers_join = ' '.join(numbers_sort)

    print(f'#{tc+1} {numbers_join}')