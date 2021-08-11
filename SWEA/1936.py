A, B = map(int, input().split())

if A - B == 2:
    print('B')
elif B - A == 2:
    print('A')
elif A > B:
    print('A')
else:
    print('B')