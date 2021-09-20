import sys

numbers = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    else:
        numbers.append(int(s))

check = [0 for _ in range(123456*2+1)]
check[1] = 1
i = 2
while i <= 123456*2: 
    j = 2 # multiply num
    while i * j <= 123456*2:
        if check[i*j] == 0:
            check[i*j] = 1
        j += 1
    i += 1

for n in numbers:
    cnt = 0
    for i in range(n+1, 2*n+1):
        if check[i] == 0:
            cnt += 1
    print(cnt)