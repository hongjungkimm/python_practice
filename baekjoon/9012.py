import sys

T = int(sys.stdin.readline())

for tc in range(T):
    bracket = sys.stdin.readline().strip()
    result = 'YES'
    if bracket.count('(') != bracket.count(')'):
        result = 'NO'
    for i in range(len(bracket) // 2):
        bracket = bracket.replace('()', '', 1)
        if len(bracket) == 0:
            result = 'YES'
            break
        if bracket.count('()') == 0:
            result = 'NO'
            break
    print(result)