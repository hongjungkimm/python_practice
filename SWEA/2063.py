T = int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)
    
if T % 2:
    print(numbers[T//2])
else:
    print((numbers[T//2-1] + numbers[T//2]) / 2)