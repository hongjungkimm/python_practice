# 팩토리얼 구하는 함수 만들기

def factorial(num): # 재귀를 이용하여 팩토리얼 만들기
    if num <= 0: # 0보다 작은 수의 팩토리얼을 모두 1로 처리
        return 1
    else:
        return num * factorial(num - 1)

num = int(input('1보다 큰 수를 입력하세요 : '))
print(factorial(num))