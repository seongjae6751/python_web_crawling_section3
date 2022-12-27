import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 요청 URL
URL = 'https://www.wishket.com/accounts/login/'

# Fake User-Agent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s:
    # URL 연결
    s.get(URL)
    # Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'seongjae6751',
        'password': 'rlatjdwo1303@',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    print('headers',s.headers)

    # 요청
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Aent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})

    # HTML 결과 a

    print('response',response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectlist = soup.select("body > div.gaia > div > div.mb60.container > div.content > div.right-side > div.mb16.user-info.user-info-partner > div.user-project")
        for i in projectlist:
            print(i)
    




