from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 클래스 이해
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=n2ll_&logNo=221442949008

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options
        chrome_options.add_argument("--headless") #CLI (user-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/section3/webdriver/chrome/chromedriver.exe')
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 $$ 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        self.driver.find_element_by_name('id').send_keys('seongjae6751')
        self.driver.find_element_by_name('pw').send_keys('rlatjdwo1303@')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(30)
        self.driver.get('https://cafe.naver.com/joonggonara')
        self.driver.find_element_by_xpath('//*[@id="NM_MY_TAB"]/div/div[1]/a[4]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_elements_by_xpath('//*[@id="menuLink47"]').click()
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!!^^*.')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a/img').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행

if __name__ == '__main__': #내부에서만 실행 됨
    #객체 생성
    a = NcafeWriteAtt()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a




    















