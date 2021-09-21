import sys

string = [i for i in sys.stdin.readline().rstrip()]
target = [i for i in sys.stdin.readline().rstrip()]

while len(string) != len(target):
    if target[-1] == 'A':
        target.pop()
    elif target[-1] == 'B':
        target.pop()
        target = target[::-1]

if target == string:
    print(1)
else:
    print(0)