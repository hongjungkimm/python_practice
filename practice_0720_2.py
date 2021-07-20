# 간단한 문자열 역순 만들기

def reverse_str(str1):
    result = ''
    for i in str1:
        result = i + result
    return result

print(reverse_str('python'))