from collections import defaultdict

def solution(m, musicinfos):
    music_dict = defaultdict(list)
    music_title = []
    for music in musicinfos:
        tmp = music.split(',')
        time = (int(tmp[1][:2]) - int(tmp[0][:2])) * 60 + (int(tmp[1][3:]) - int(tmp[0][3:]))
        title = tmp[2]
        notes = tmp[3]
        music_title.append(title)
        music_dict[title].append(time)
        music_dict[title].append(title)
        music_dict[title].append(notes)
    
    music_true = defaultdict(int)
    for music in music_title:
        notes = music_dict[music][2]
        tmp = notes * len(notes)
        if m in tmp:
            if len(m) == len(tmp):
                music_true[music] = 1
            else:
                idx = tmp.index(m)
                if tmp[idx + len(m)] != '#':
                    music_true[music] = 1
                else:
                    music_true[music] = 0
        else:
            music_true[music] = 0
        # idx = notes.index(m[0])
        # cnt = len(m) + 1
        # stack = []
        # while cnt:
        #     stack.append(notes[idx])
        #     idx += 1
        #     cnt -= 1
        #     if idx == len(notes):
        #         idx = 0
        # stack = ''.join(stack)
        # if m in stack:
        #     if stack[-1] != '#':
        #         music_true[music] = 1
        #     else:
        #         music_true[music] = 0
        # else:
        #     music_true[music] = 0

    answer = ''
    time = 0
    for music in music_title:
        if music_true[music] and music_dict[music][0] > time:
            time = music_dict[music][0]
            answer = music
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))