first_num = int(input())

result_list = []
max_cnt = 0
i = 0
while i < first_num + 1:
    num_list = [first_num]
    i += 1
    num_list.append(i)
    while num_list[-1] >= 0:
        num_list.append(num_list[-2] - num_list[-1])
    if len(num_list) > max_cnt:
        max_cnt = len(num_list)
        result_list = num_list[:-1]

print(max_cnt-1)
for n in result_list:
    print(n, end=' ')