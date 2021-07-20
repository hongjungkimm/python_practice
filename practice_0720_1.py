# 리스트의 중앙값(중간값) 구하기

numbers = list(map(int, input('숫자를 입력하세요. ex) 5 3 7 6 8: ').split()))
numbers = sorted(numbers)
    
if len(numbers) % 2:
    print(numbers[len(numbers)//2]) # 리스트의 길이가 홀수일 때는 인덱스 기준으로 절반
else:
    print((numbers[len(numbers)//2-1] + numbers[len(numbers)//2]) / 2) # 리스트의 길이가 짝수일 때는 인덱스 기준으로 절반보다 하나 앞의 값과 절반 값 나누기 2