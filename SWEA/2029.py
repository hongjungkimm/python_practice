T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    print(f'#{tc+1} {a//b} {a%b}')