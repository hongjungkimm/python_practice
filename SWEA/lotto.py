import random

# 2 9 10 14 22 44 (8월 21일 당첨 번호)
my_lucky_nums = list(map(int, input('행운의 번호 6자리를 띄어쓰기로 구분하여 입력해주세요: ').split()))

round = 0
while True:
    round += 1
    lotto_nums = random.sample(range(1, 46), 6)
    matched = len(set(my_lucky_nums) & set(lotto_nums))

    if matched == 6:
        print('축하합니다! 로또 1등 당첨입니다!!!!!!!!!! 🎉🎉🎉🎉')
        break
    
    print(f'로또 구입 {round}회차...! 현재까지 쓴 돈 {round * 1000}')
    print(lotto_nums)