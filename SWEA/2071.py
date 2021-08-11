T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))
    sum_num = sum(numbers)
    avg_num = int(round(sum(numbers) / len(numbers), 0))
    
    print(f'#{tc+1} {avg_num}')