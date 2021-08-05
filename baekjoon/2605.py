import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(len(numbers)):
    if i+1 == 1:
        result.append(str(i+1))
    else:
        result.insert(i-numbers[i], str(i+1))

print(" ".join(result))