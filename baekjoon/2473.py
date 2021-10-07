import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
min_num = float('inf')
result = []

for i in range(N-2):
    start, end = i+1, N-1

    flag = False
    while start < end:
    
        if abs(numbers[i] + numbers[start] + numbers[end]) < min_num:
            min_num = abs(numbers[i] + numbers[start] + numbers[end])
            result = [i, start, end]
        
        if numbers[i] + numbers[start] + numbers[end] > 0:
            end -= 1
        elif numbers[i] + numbers[start] + numbers[end] < 0:
            start += 1
        else:
            flag = True
            break

    if flag:
        break

print(numbers[result[0]], numbers[result[1]], numbers[result[2]])