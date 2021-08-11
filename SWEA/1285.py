T = int(input())

for tc in range(T):
    person = int(input())
    rocks = list(map(int, input().split()))

    rocks_list = []
    for rock in rocks:
        rocks_list.append(abs(0 - rock))
    
    print(f'#{tc+1} {min(rocks_list)} {rocks_list.count(min(rocks_list))}')
