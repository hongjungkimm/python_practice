import sys

calculation = sys.stdin.readline().rstrip()

cal_list = []
tmp = ''
i = 0
while True:
    if calculation[i].isdigit():
        if i == len(calculation) - 1:
            tmp += calculation[i]
            cal_list.append(tmp)
            break
        if calculation[i+1].isdigit():
            tmp += calculation[i]
            i += 1
        else:
            tmp += calculation[i]
            cal_list.append(tmp)
            tmp = ''
            i += 1
    else:
        cal_list.append(calculation[i])
        i += 1

result = int(cal_list[0])
minus = False
i = 2
while i < len(cal_list):
    if cal_list[i-1] == '-':
        minus = True
        result -= int(cal_list[i])
        i += 2
    else:
        if minus:
            result -= int(cal_list[i])
            i += 2
        else:
            result += int(cal_list[i])
            i += 2

print(result)