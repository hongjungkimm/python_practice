import sys

len_A, len_B = map(int, sys.stdin.readline().split())
input_A = list(map(int, sys.stdin.readline().split()))
input_B = list(map(int, sys.stdin.readline().split()))

result = input_A + input_B
result.sort()
print(' '.join(list(map(str, result))))