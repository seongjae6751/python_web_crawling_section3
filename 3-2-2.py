import requests

# Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code) # 상태 값을 출력(404, 200, ...)
print(r.ok) 

# https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1') # json관련 테스트 사이트
# print(r.text)
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content) # 바이트 값으로 가져옴
print(r.raw) # raw 값으로 가져옴


















