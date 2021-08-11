T = int(input())

for tc in range(T):
    date = input()
    
    if int(date[4:6]) > 12 or int(date[4:6]) < 1:
        print(f'#{tc+1} -1')
    elif int(date[4:6]) == 1 or int(date[4:6]) == 3 or int(date[4:6]) == 5 or int(date[4:6]) == 7 or int(date[4:6]) == 8 or int(date[4:6]) == 10 or int(date[4:6]) == 12:
        if int(date[6:]) < 1 or int(date[6:]) > 31:
            print(f'#{tc+1} -1')
        else:
            print(f'#{tc+1} {date[:4]}/{date[4:6]}/{date[6:]}')
    elif int(date[4:6]) == 2:
        if int(date[6:]) < 1 or int(date[6:]) > 28:
            print(f'#{tc+1} -1')
        else:
            print(f'#{tc+1} {date[:4]}/{date[4:6]}/{date[6:]}')
    else:
        if int(date[6:]) < 1 or int(date[6:]) > 30:
            print(f'#{tc+1} -1')
        else:
            print(f'#{tc+1} {date[:4]}/{date[4:6]}/{date[6:]}')