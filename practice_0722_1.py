# 재귀를 이용하여 로그인 기능 만들기

# 로그인할 때 아이디와 비밀번호가 달라야 한다고 가정
def login():
    user_id = input('아이디를 입력하세요: ')
    user_pw = input('비밀번호를 입력하세요: ')

    if user_id != user_pw:
        return f'{user_id} 님 성공적으로 로그인 되셨습니다 :)'

    return login()

print(login())