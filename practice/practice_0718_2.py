# 피보나치 수열 만들기

def make_fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return make_fibonacci(num - 1) + make_fibonacci(num - 2) # n번째 수는 n-1, n-2번째 수를 더한 수 

num = int(input("숫자를 입력하세요: "))
num_list = []
for i in range(1, num + 1):
    num_list.append(make_fibonacci(i))

print(num_list)