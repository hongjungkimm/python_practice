T = int(input())

for tc in range(1, T+1):
    sentence = input()

    inspection = []
    result = 1
    for i in range(len(sentence)):
        if sentence[i] == '(':
            inspection.append(sentence[i])
        elif sentence[i] == '{':
            inspection.append(sentence[i])
        elif sentence[i] == ')':
            if len(inspection) == 0:
                result = 0
                break
            elif inspection[-1] == '(':
                inspection.pop()
            else:
                result = 0
                break
        elif sentence[i] == '}':
            if len(inspection) == 0:
                result = 0
                break
            elif inspection[-1] == '{':
                inspection.pop()
            else:
                result = 0
                break

    if inspection:
        result = 0
        
    print('#{0} {1}'.format(tc, result))