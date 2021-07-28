# 2차원 배열 분해 및 재조합하기

arr = [[1, 2, 3, 4, 5, 6],
       [7, 8, 9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18]
]

# 세로로 묶음
vertical = []

for i in range(6):
    temp = []
    for line in arr:
        temp.append(line[i])
    vertical.append(temp)

print(vertical)

# 정사각형으로 묶음
square = []

for i in range(2):
    temp = []
    for line in arr:
        for n in line[i*3:(i+1)*3]:
            temp.append(n)
    square.append(temp)

print(square)
