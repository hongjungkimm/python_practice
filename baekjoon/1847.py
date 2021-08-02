import sys # 시간초과로 실패

n = int(sys.stdin.readline())

stack = [0]
remainder = [0]
result = []
for _ in range(n):
    number = int(sys.stdin.readline())
    if number == stack[-1]:
        remainder.append(stack[-1])
        stack = stack[:-1]
        result.append('-')

    elif number < stack[-1]:
        result.append('NO')

    else:
        i = max(remainder) + 1
        while i < number+1:
            stack.append(i)
            result.append('+')
            i += 1
        remainder.append(stack[-1])
        stack = stack[:-1]
        result.append('-')
    
for i in result:
    if i == 'NO':
        print('NO')
    else:
        for i in result:
            print(i)