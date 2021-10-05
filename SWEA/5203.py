T = int(input())

for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(0, len(temp), 2):
        player1.append(temp[i])
        player2.append(temp[i+1])

    player1_victory = False
    player2_victory = False

    player1_play = []
    player2_play = []
    for i in range(6):
        player1_play.append(player1[i])
        if len(player1_play) > 2:
            player1_temp = sorted(player1_play)
            for j in range(len(player1_temp)-2):
                if player1_temp.count(player1_temp[j]+1) and player1_temp.count(player1_temp[j]+2):
                    player1_victory = True
                    break
                elif player1_temp[j] == player1_temp[j+1] and player1_temp[j] == player1_temp[j+2]:
                    player1_victory = True
                    break

        player2_play.append(player2[i])
        if len(player2_play) > 2:
            player2_temp = sorted(player2_play)
            for j in range(len(player2_temp)-2):
                if player2_temp.count(player2_temp[j] + 1) and player2_temp.count(player2_temp[j] + 2):
                    player2_victory = True
                    break
                elif player2_temp[j] == player2_temp[j+1] and player2_temp[j] == player2_temp[j+2]:
                    player2_victory = True
                    break

        if player1_victory or player2_victory:
            break

    if player1_victory:
        print('#{0} 1'.format(tc))
    elif player2_victory:
        print('#{0} 2'.format(tc))
    else:
        print('#{0} 0'.format(tc))