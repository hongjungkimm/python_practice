# 재귀를 이용하여 10진수를 2진수로 변환하기

def make_binary(decimal_num):
    if decimal_num <= 1:
        return str(decimal_num)
    else:
        return make_binary(decimal_num//2) + str(decimal_num%2)