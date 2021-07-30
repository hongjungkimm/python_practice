N, M = map(int, input().split())

url_pw_dict = {}
for i in range(N):
    url_pw = list(map(str, input().split()))
    url_pw_dict[url_pw[0]] = url_pw[1]

search_list = []
for i in range(M):
    user = input()
    search_list.append(url_pw_dict[user])

for i in search_list:
    print(i)