import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

cnt = 0
for word in words:
    w_dict = {key: [] for key in word}
    for i in range(len(word)):
        if word[i] in w_dict:
            w_dict[word[i]].append(i)
    
    flag = False
    for v in w_dict.values():
        if len(v) > 1:
            for i in range(len(v)-1):
                if v[i+1] - v[i] != 1:
                    flag = True
                    break
        if flag:
            break
    else:
        cnt += 1

print(cnt)