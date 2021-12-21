# 10개 중에 8개 통과, 2개 실패
def solution(N, number):
    def make_min_cnt(current):
        nonlocal nums, number, answer, tmp_nums, tmp_cnts
        cnt = 0
        for i in range(len(tmp_nums)):
            if tmp_nums[i] == current:
                cnt = tmp_cnts[i]
                break
        
        if cnt > 8:
            return

        if current == number:
            if answer > cnt:
                answer = cnt
            return

        current_idx = tmp_nums.index(current)
        for i in range(1, len(nums)):
            if current + int(nums[i]) not in tmp_nums:
                tmp_nums.append(current + int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current + int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current + int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current + int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current - int(nums[i]) not in tmp_nums:
                tmp_nums.append(current - int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current - int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current - int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current - int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current * int(nums[i]) not in tmp_nums:
                tmp_nums.append(current * int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current * int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current * int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current * int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current // int(nums[i]) not in tmp_nums:
                tmp_nums.append(current // int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current // int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current // int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current // int(nums[i]))
                    tmp_cnts = origin

    nums = [0]
    answer = float('inf')
    for i in range(8):
        nums.append(str(N) + str(N) * i)
    tmp_nums = []
    tmp_cnts = []
    for i in range(1, len(nums)):
        if nums[i] not in tmp_nums:
            tmp_nums.append(int(nums[i]))
            tmp_cnts.append(i)
        else:
            if tmp_cnts[nums[i]] > 1:
                tmp_cnts[nums[i]] = 1
        make_min_cnt(int(nums[i]))

    if answer == float('inf'):
        return -1
    return answer

print(solution(5, 12))
print(solution(2, 11))



# 참고 코드
def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1


print(solution(2, 11))