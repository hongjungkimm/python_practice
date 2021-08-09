# 카운팅 정렬

listA = [1, 3, 4, 5, 7, 5, 4, 2, 8, 1, 2, 6]

listB = [0] * 9
for i in range(len(listA)):
    listB[listA[i]] += 1

for i in range(1, len(listB)):
    listB[i] += listB[i-1]

listC = [0] * 12
for i in range(len(listA)-1, -1, -1):
    listC[listB[listA[i]]-1] = listA[i]
    listB[listA[i]] -= 1

print(listC)