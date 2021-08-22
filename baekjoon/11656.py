import sys

string = sys.stdin.readline().rstrip()

strings = []
tmp = ''
for s in string[::-1]:
    tmp = s + tmp
    strings.append(tmp)

strings.sort()
for s in strings:
    print(s)