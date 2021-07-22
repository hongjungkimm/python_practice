# 리스트 오름차순 정렬시키기

list = [3, 6, 7, 5, 9, 0, 1, 2, 10, 8, 0, 17, 20, 2, 1, 100, 15]

for i in range(len(list)):
    for e in range(i+1, len(list)):
        if list[i] > list[e]:
            list[i], list[e] = list[e], list[i]

print(list)