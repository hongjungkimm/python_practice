word = input().upper()

word_list = list(set(word))
cnt_list = []
for i in word_list:
    cnt_list.append(word.count(i))

if cnt_list.count(max(cnt_list)) >= 2:
    print('?')
else:
    print(word_list[cnt_list.index(max(cnt_list))])