import requests, json

# r = requests.get('https://api.github.com/events')
# r.raise_for_status() # 예외를 제외시켜줌
# print(r.text)

jar = requests.cookies.RequestsCookieJar() # 쿠키를 설정 및 인스턴스 화
jar.set('name', 'kim', domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status
# print(r.text)

# r = requests.get('https://github.com',timeout=3) # 서버가 반응할때까지 대기하겠다는 뜻 
# print(r.text)

# 공문의 내용이 많을때는 post 많이 사용, 데이터를 서버에 저장하는 형식
# post = r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar) # -> httpbin에 이 데이터를 저장하라고 보냄
# print(r.text)

payload1 = {'key1':'value1','key2':'value2'} # 딕셔너리 
payload2 = (('key1','value1'),('key2','value2')) # 튜플
payload3 = {'some':'nice'}

r = requests.post('http://httpbin.org/post',data=payload1) # form 값이 아닌 json 형태로 파알을 받음
print(r.text)

r = requests.post('http://httpbin.org/post',data=json.dumps(payload3)) # form 값이 아닌 json 형태로 파알을 받음
print(r.text)

# form 데이터와 json 데이터의 차이
# -> https://velog.io/@ryan-son/multipartform-data-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-vs-applicationjson



