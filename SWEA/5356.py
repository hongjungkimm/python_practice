T = int(input())

for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    
    chg_words = []
    for word in words:
        chg_words.append(word + '-' * (max_len - len(word)))

    result = ''
    for i in range(max_len):
        for word in chg_words:
            result += word[i]
    
    result = result.replace('-', '')
    print('#{0} {1}'.format(tc, result))