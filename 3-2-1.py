import requests

s = requests.Session() # session(사이트)정보를 가져옴
# r = s.get('https://naver.com') # PUT, DELETE, GET, POST
# print('1',r.text)

# r = s.get('http://httpbin.org/cookies',cookies={'from':'myname'})
# print(r.text)

url = 'http://httpbin.org/get' # get과 post등을 점검할수 있는 테스트 사이트
headers = {"user-agent" : 'myPythonApp_1.0.0'}

# r = s.get(url,headers=headers)
# print(r.text)

s.close()

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)