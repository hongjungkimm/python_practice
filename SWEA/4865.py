T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_counting = [0 for _ in range(len(str1))]

    for i in range(len(str1)):
        for s in str2:
            if str1[i] == s:
                str1_counting[i] += 1

    max_num = str1_counting[0]
    for c in str1_counting:
        if c > max_num:
            max_num = c

    print('#{0} {1}'.format(tc, max_num))