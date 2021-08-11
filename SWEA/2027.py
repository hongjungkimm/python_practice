list1 = ['+', '+', '+', '+', '+']

for i in range(len(list1)):
    list1[i] = '#'
    for e in range(len(list1)):
        print(list1[e], end='')
    print()
    list1[i] = '+'