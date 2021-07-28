# 연속으로 중복되는 숫자 삭제하고 반환

def not_contin_repe(list1):
    result = [list1[0]]

    for n in list1:
        if result[-1] != n:
            result.append(n)
    return result

print(not_contin_repe([3, 3, 3, 4, 4, 1, 2, 3, 3, 5, 5, 6])) # [3, 4, 1, 2, 3, 5, 6]