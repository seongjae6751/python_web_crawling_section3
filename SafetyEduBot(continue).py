from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class listenSafetyEdu:
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/section3/webdriver/chrome/chromedriver.exe')
        self.driver.implicitly_wait(5)

    def loginAndListen(self):
        self.driver.get('https://edu.labs.go.kr/front/membership/login.do')
        self.driver.find_element_by_name('userid').send_keys('seongjae4402')
        self.driver.find_element_by_name('userpass').send_keys('rlatjdwo4402@')
        self.driver.find_element_by_xpath('//*[@id="form1"]/div/a').click()
        self.driver.implicitly_wait(5)
        self.driver.get('https://edu.labs.go.kr/front/my/lecture.do')
        self.driver.find_element_by_xpath('//*[@id="mform"]/table/tbody/tr/th/div/h5/a').click()
        self.driver.execute_script('document.querySelector("#lctWrap > div.lctCont > div.lctcWeek > table:nth-child(2) > tbody > tr > td:nth-child(2) > ul > li.lctc1 > a")')

if __name__ == '__main__':
    a = listenSafetyEdu()
    a.loginAndListen()

