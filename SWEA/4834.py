T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = int(input())

    card = []
    for _ in range(N): # number를 반복해서 10으로 나눈 후의 나머지를 card 리스트에 추가
        card.append(number % 10)
        number = number // 10

    count_card = [0] * 10 # 0~9까지의 빈 숫자 카운트 리스트를 생성
    for i in range(N):
        count_card[card[i]] += 1 # 각 숫자의 자리에 1씩 더해줌

    card_index = 0 # 각 카운트가 큰 숫자의 인덱스를 찾기 위한 변수 생성(맨 앞부터 차근차근)
    for i in range(len(count_card)):
        if count_card[i] >= count_card[card_index]:
            card_index = i # 카운트가 가장 큰 인덱스를 card_index에 저장

    print('#{0} {1} {2}'.format(tc, card_index, count_card[card_index]))