# 소수 판별 함수 만들기

def is_prime(num): # 소수 판별을 위한 숫자 입력
    cnt = 0 # 자신보다 작은 수로 나누었을 때 나머지가 0이 되는지 세기 위한 변수
    if num == 1:
        print(f'{num}은 소수가 아닙니다.')
    elif num == 2:
        print(f'{num}은 소수 입니다.')
    else:
        for i in range(2, num): # 반복해서 자신보다 작은 수(1인 제외)로 나누어 나머지가 0이 되는 수가 있는지 확인
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            print(f'{num}은 소수 입니다.')
        else:
            print(f'{num}은 소수가 아닙니다.')

num = int(input("양의 정수를 입력하세요: "))
is_prime(num)