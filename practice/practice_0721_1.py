# 위치인자, 기본인자, 가변 키워드 인자 이용 함수 만들기

def make_url(id, name='python', **kwargs):
    BASE_URL = 'https://hongjungkimm.com?'
    BASE_URL = BASE_URL + id + f'&name={name}'
    
    for key, value in kwargs.items():
        BASE_URL = BASE_URL + f'&{key}={value}'
    
    return BASE_URL

print(make_url('12345678', name='java', date='0721', status='open'))
