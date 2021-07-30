import sys

N = int(sys.stdin.readline()) # 약수의 개수

divisor = list(map(int, sys.stdin.readline().split()))

print(min(divisor) * max(divisor))