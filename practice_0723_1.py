# 대칭을 이루는 문자열 찾는 함수 만들기

# func1
def is_symmetry(str1):
    if str1 == str1[::-1]:
        return True
    return False

# func2
def is_symmetry2(str1):
    if len(str1) % 2:
        if len(str1) == 1:
            return True
        if str1[0] == str1[-1]:
            return is_symmetry2(str1[1:-1])
        else:
            return False
    
    else:
        if len(str1) == 2 and str1[0] == str1[1]:
            return True
        else:
            return False
        if str1[0] == str1[-1]:
            return is_symmetry2(str1[1:-1])