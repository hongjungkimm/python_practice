# 버블정렬

list1 = [78, 34, 23, 12, 7, 0, 6, 34, 55, 89, 2, 4, 0]

for i in range(len(list1)-1, 0, -1):
    for j in range(i):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)
