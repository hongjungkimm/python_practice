T = int(input())

for tc in range(T):
    date = list(map(int, input().split()))

    date_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if date[0] == date[2]:
        print(f'#{tc+1} {date_dict[date[0]] - date[1] + 1}')
    else:
        result = date[3] + (date_dict[date[0]] - date[1]) + 1
        i = date[0] + 1
        while i < date[2]:
            result += date_dict[i]
            i += 1
        print(f'#{tc+1} {result}')
