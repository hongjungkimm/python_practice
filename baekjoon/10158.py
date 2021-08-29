import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline().split())

x_move = t % (w * 2)
y_move = t % (h * 2)

tmp_x = p + x_move
tmp_y = q + y_move

if w < tmp_x <= w * 2:
    tmp_x = w * 2 - tmp_x

if h < tmp_y <= h * 2:
    tmp_y = h * 2 - tmp_y

final_x = tmp_x % (w * 2)
final_y = tmp_y % (h * 2)

print(final_x, final_y)