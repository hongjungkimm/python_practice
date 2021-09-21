import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

i = 0
flag = False
while i <= len(S) - len(P):
    if S[i] == P[0]:
        j = i
        for p in P:
            if S[j] == p:
                j += 1
            else:
                break
        else:
            flag = True
    if flag:
        break
    i += 1

if flag:
    print(1)
else:
    print(0)