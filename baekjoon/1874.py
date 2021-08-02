import sys

n = int(sys.stdin.readline())

stack = []
operation = []
cnt = 1
possible = True

for _ in range(n):
    number = int(sys.stdin.readline())
    while cnt <= number:
        stack.append(cnt)
        operation.append('+')
        cnt += 1
    if stack[-1] == number:
        stack.pop()
        operation.append('-')
    else:
        possible = False

if possible == False:
    print('NO')
else:
    for i in operation:
        print(i)