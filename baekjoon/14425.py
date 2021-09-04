import sys

N, M = map(int, sys.stdin.readline().split())

n_list = [sys.stdin.readline().rstrip() for _ in range(N)]
m_list = [sys.stdin.readline().rstrip() for _ in range(M)]
m_dict = {key:0 for key in m_list}

for m in m_list:
    m_dict[m] += 1
s_n_list = set(n_list)
s_m_list = set(m_list)

remainder = set(s_m_list - s_n_list)
result = list(s_m_list - remainder)

cnt = 0
for r in result:
    cnt += m_dict[r]

print(cnt)