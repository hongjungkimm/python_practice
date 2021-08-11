T = int(input()) # Test Case 개수

for tc in range(T):
    # 이 아래부터 실질적인 코드 작성
    numbers = list(map(int, input().split()))
    
    total = 0
    for number in numbers:
        if number % 2:
            total += number
    
    print(f'#{tc+1} {total}')