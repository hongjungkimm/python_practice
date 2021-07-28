N, K = map(int, input().split())

coins = []
for n in range(N):
    coin = int(input())
    coins.append(coin)

coins_rv = list(reversed(coins))
total = 0
i = 0
while K != 0:
    if K // coins_rv[i] >= 1:
        total += K // coins_rv[i]
        K = K % coins_rv[i]
    i += 1

print(total)