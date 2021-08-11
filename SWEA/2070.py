T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    if a > b:
        print(f'#{tc+1} >')
    elif b > a:
        print(f'#{tc+1} <')
    else:
        print(f'#{tc+1} =')