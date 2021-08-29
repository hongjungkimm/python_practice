import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

p_move = t % (w * 2)
q_move = t % (h * 2)

p_tmp = p + p_move
q_tmp = q + q_move

if w < p_tmp <= w * 2:
    p_tmp = w * 2 - p_tmp

if h < q_tmp <= h * 2:
    q_tmp = h * 2 - q_tmp

p_result = p_tmp % (w * 2)
q_result = q_tmp % (h * 2)

print(p_result, q_result)