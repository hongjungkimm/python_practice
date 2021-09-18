import sys

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

num_dict1 = {k:0 for k in numbers}
result = 0
i = 0
j = 0
while i < N:
    num_dict1[numbers[i]] += 1
    if num_dict1[numbers[i]] > K:
        if result < i - j:
            result = i - j
        while num_dict1[numbers[i]] > K:
            num_dict1[numbers[j]] -= 1
            j += 1
    i += 1

if i - j > result:
    result = i - j
print(result)