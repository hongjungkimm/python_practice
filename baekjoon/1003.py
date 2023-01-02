import sys

T = int(sys.stdin.readline())
tc_list = []
for _ in range(T):
    N = int(sys.stdin.readline())
    tc_list.append(N)

def fibonacci(n, zero_cnt, one_cnt):
    return

for x in tc_list:
    if x == 0:
        print(1, 0)
    elif x == 1:
        print(0, 1)
    elif x == 2:
        print(1, 1)
    else:
        zero_list = [0, 1]
        one_list = [1, 1]
        for _ in range(x-2):
            zero_list.append(zero_list[-1] + zero_list[-2])
            one_list.append(one_list[-1] + one_list[-2])
        print(zero_list[-1], one_list[-1])
        