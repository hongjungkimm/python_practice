import sys

N, K = map(int, sys.stdin.readline().split())
temperatures = list(map(int, sys.stdin.readline().split()))

sum_list = [sum(temperatures[:K])]
tmp = sum_list[0]

index_f, index_b = 0, K
for i in range(1, N-K+1):
    tmp = tmp - temperatures[index_f] + temperatures[index_b]
    index_f += 1
    index_b += 1
    sum_list.append(tmp)
print(max(sum_list))