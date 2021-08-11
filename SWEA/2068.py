T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))

    print(f'#{tc+1} {max(numbers)}')