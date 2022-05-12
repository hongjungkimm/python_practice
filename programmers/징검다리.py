def solution(distance, rocks, n):
    rocks.sort()
    answer = 0
    start = 0
    end = distance
    while start <= end:
        mid = (start + end) // 2
        del_rock = 0
        standard_rock = 0
        for rock in rocks:
            if rock - standard_rock < mid:
                del_rock += 1
            else:
                standard_rock = rock
            if del_rock > n:
                break
        if del_rock > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
