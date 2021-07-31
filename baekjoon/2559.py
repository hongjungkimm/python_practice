# 1번째 방법
import sys

N, K = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

if K == 1:
    print(max(temperatures))
else:
    result_list = []
    for i in range(N-K+1):
        result_list.append(sum(temperatures[i:K+i]))

    print(max(result_list))


# 2번째 방법
import sys

N, K = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

result_list = []
i = 0
for i in range(N-K+1):
    tmp = 0
    for j in range(K):
        tmp += temperatures[i+j]
    result_list.append(tmp)

print(max(result_list))