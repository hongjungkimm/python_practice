T = int(input())

for tc in range(T):
    num_stu, done_stu = list(map(int, input().split()))
    done_list = list(map(int, input().split()))
    
    all_stu_list = list(range(1, num_stu+1))
    all_stu_list = set(all_stu_list)
    done_list = set(done_list)
    f_list = all_stu_list - done_list
    f_list = list(f_list)
    f_list = sorted(f_list)

    f_stu = ''
    for i in f_list:
        temp = str(i) + " "
        f_stu += temp

    print(f'#{tc+1} {f_stu[:-1]}')