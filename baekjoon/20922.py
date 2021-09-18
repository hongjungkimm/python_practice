import sys # 시간초과

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

num_dict1 = {k:0 for k in numbers}
result = 0
length = 0
i = 0
j = 0
while i < N:
    num_dict1[numbers[i]] += 1
    length += 1
    if num_dict1[numbers[i]] > K:
        if result < length - 1:
            result = length - 1
        num_dict1 = {k:0 for k in numbers}
        length = 0
        j += 1
        i = j - 1
    i += 1
if result < length:
    result = length

print(result)