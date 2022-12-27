# import sys,io, re, time, threading, schedule
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# class NoticeNotification:
#     """
#     한국기술교육대학교 공지사항 알리미
#     Author : Seongjae
#     Date:
#     """

#     # 초기(webdriver) 설정
#     def __init__(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless") #CLI (user-agent)
#         chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#         self.driver = webdriver.Chrome(chrome_options=chrome_options,  executable_path = 'C:/section3/webdriver/chrome/chromedriver.exe')
#         self.driver.implicitly_wait(30)

#     # 키워드 입력
#     def inputKeyword(self):
#         self.keyword = []
#         self.a = input("키워드를 입력하시겠습니가? (y/n)")
#         while self.a == 'y':
#            if self.a == 'y':
#               self.i = input('키워드를 입력하세요:')
#               self.keyword.append(self.i)
#               print(self.keyword)
#               self.i2 = input("더 입력하시겠습니까? (y/n)")
#               if self.i2 == 'y':
#                 continue
#               elif self.i2 == 'n':
#                 break
#               else:
#                 print('y나 n중에 선택하세요')
#                 continue
#            elif self.a == 'n':
#                break
#            else:
#               print('y나 n중에 선택하세요')
#               continue

#     # 키워드로 검색
#     def searchKeyword(self):
#         self.driver.get('https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?robot=Y&mCode=MN230&page=1')
#         self.driver.implicitly_wait(30)
#         soup = BeautifulSoup(self.driver.page_source, 'html.parser')
#         self.driver.implicitly_wait(30)
#         self.table = soup.find('table', {'class': 'board-list-table'})
#         keyword_list = []
#         for i in self.keyword:
#           keyword_list.extend(self.table.find_all('span', title=re.compile(i)))
#         for i2, e in enumerate(keyword_list):
#           print(i2+1, e.get_text())


#     # 소멸자
#     def __del__(self):
#         #self.driver.close() #현재 실행 포커스 된 영역을 종료
#         self.driver.quit()  #Seleninum 전체 프로그램 종료
#         print("Removed driver Object")

# # 실행
# if __name__ == '__main__':
#     d = NoticeNotification()
#     d.inputKeyword()
#     d.searchKeyword()

import sys, re, requests, json
from bs4 import BeautifulSoup
import urllib.request as req

"""
    요구사항
    0. 한기대 서버로 부터 크롤링
    1. 새로운 결과 있다면 출력 : [title, url, Date] 
    2. 새로운 결과가 없다면 출력 : ["noResult"]
    3. 가장 최근 공지 고유번호 설정(변화가 없으면 안해도됨.)
"""

generalnotice = "https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/list.do?mCode=MN230"
scholarnotice = "https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/scholarList.do?mCode=MN231"
bachelornotice = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/bachelorList.do?mCode=MN233'
employmentnotice = 'https://www.koreatech.ac.kr/kor/CMS/NoticeMgr/boardList10.do?mCode=MN445'
noticelist = [generalnotice, scholarnotice, bachelornotice, employmentnotice]
useridlink = 'http://uskawjdu.iptime.org:8084/query/USER?userid='
userkeywordlink = 'http://uskawjdu.iptime.org:8084/query/KEYWORD?userid='
userid = 4

def noticeNotification(userid):
    # 유저 키워드 가져오기
    r1 = requests.get(userkeywordlink + str(userid))
    j1 = json.loads(r1.text)
    r2 = requests.get(useridlink + str(userid))
    j2 = json.loads(r2.text)
    filldict = {j1[i]['listcode'] : j1[i]['keyword'] for i in range(len(j1))}
    def noticeCrawling(noticeurl):
        res = req.urlopen(noticeurl).read()
        soup = BeautifulSoup(res, "html.parser")
        table = soup.find('table', {'class': 'board-list-table'})
        tbody = table.select_one('tbody')
        trs = tbody.select('tr')
        lastnum = j2[0]['lastCrawling'+noticeurl[-5:]]
        numlist = []
        title = soup.find('h2', {'class':'cont-tit'}).text
        for tr in trs:
            numb = tr.select('td')[0].text
            numlist.append(int(numb))
        try:
            for tr in trs:
                number = tr.select('td')[0].text
                if int(number) > int(lastnum):
                    link = tr.find('a').attrs['href']
                    name = tbody.find_all('span',title=re.compile(filldict[noticeurl[-5:]]))
                    if noticeurl[-5:] == 'MN230':
                        nation = tr.select('td')[3].text
                        print('---'+title+'---\n', name[0].string , '\n공지 접속: https://www.koreatech.ac.kr'+link, '\n---'+nation+'---')
                    else: 
                        nation = tr.select('td')[2].text
                        print('---'+title+'---\n', name[0].string , '\n공지 접속: https://www.koreatech.ac.kr'+link, '\n---'+nation+'---')
                    requests.put(useridlink + str(userid) + '&lastCrawling' + noticeurl[-5:] + '=' + str(max(numlist)))
                    break
                elif int(number) == int(lastnum):
                    print('None')
                    requests.put(useridlink + str(userid) + '&lastCrawling' + noticeurl[-5:] + '=' + str(max(numlist)))
                    break
                    
        except IndexError:
            print('None')
    for noticeurl in noticelist:
        noticeCrawling(noticeurl)

def getAvgs():
    return [i for i in sys.argv]


if __name__=="__main__" :
    userId = getAvgs()[0]
    noticeNotification(userid)
    # python Crawling.py userid













