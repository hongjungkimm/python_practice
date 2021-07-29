a, b = map(str, input().split())

a10 = 0
for i in range(len(a)):
    a10 += ((2 ** i) * int(a[::-1][i]))

b10 = 0
for i in range(len(b)):
    b10 += ((2 ** i) * int(b[::-1][i]))

result10 = a10 + b10

def binary(n):
    if n <= 1:
        return n
    else:
        return str(binary(n//2)) + str(n%2)

print(binary(result10))