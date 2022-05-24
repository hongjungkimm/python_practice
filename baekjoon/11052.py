import sys

N = int(sys.stdin.readline())
cards_list =  [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + cards_list[j])

print(dp[N])

# import sys
# from collections import defaultdict

# def find_max(cnt, amount):
#     global N, cards_dict, max_amount

#     if cnt == 0:
#         if amount > max_amount:
#             max_amount = amount
#         return
    
#     if cnt > 0:
#         for i in range(1, cnt + 1):
#             find_max(cnt - i, amount + cards_dict[i])


# N = int(sys.stdin.readline())
# cards_list = list(map(int, sys.stdin.readline().split()))
# cards_dict = defaultdict(int)
# for i in range(N):
#     cards_dict[i+1] = cards_list[i]

# max_amount = 0
# find_max(N, 0)

# print(max_amount)