import sys

words = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
n = len(word)

cnt = 0
i = 0
while i < len(words):
    if words[i:i+n] == word:
        cnt += 1
        i += n
    else:
        i += 1

print(cnt)