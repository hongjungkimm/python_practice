# 직각삼각형 판별 함수 만들기

def is_right_angled_triangle(a, b, c): # 밑변, 높이, 빗변을 변수로 입력
    if a <= 0 or b <= 0 or c <= 0: # 밑변, 높이, 빗변 중 하나라도 0이하인 수를 입력하면 오류로 판별
        return 'Invalid value entered'
    elif a ** 2 + b ** 2 == c ** 2: # 피타고라스의 정리를 이용하여 직각삼각형 판별
        return 'Yes, it\'s a right angled triangle.'
    else:
        return 'No, it\'s not a right angled triangle.'

a, b, c = map(int, input("밑변, 높이, 빗변 순으로 입력하세요. ex) 3, 4, 5 : ").split(", "))
print(is_right_angled_triangle(a, b, c))