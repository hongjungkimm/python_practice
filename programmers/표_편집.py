def solution(n, k, cmd):
    answer = ['O'] * n
    delete = []
    point = k
    for c in cmd:
        c = c.split(" ")
        if c[0] == "U":
            num = int(c[1])
            while num > 0:
                point -= 1
                if answer[point] == 'O':
                    num -= 1
        elif c[0] == "D":
            num = int(c[1])
            while num > 0:
                point += 1
                if answer[point] == 'O':
                    num -= 1
        elif c[0] == "C":
            answer[point] = 'X'
            delete.append(point)
            while True:
                point += 1
                flag = False
                if point == n:
                    flag = True
                    while True:
                        point -= 1
                        if answer[point] == 'O':
                            break
                if flag:
                    break
                if answer[point] == 'O':
                    break
        else:
            tmp = delete.pop()
            answer[tmp] = 'O'

    answer = ''.join(answer)
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))