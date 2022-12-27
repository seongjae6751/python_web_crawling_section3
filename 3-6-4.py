from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument("--headless") #CLI(백엔드로 작동)

# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:/section3/webdriver/chrome/chromedriver.exe')
driver = webdriver.Chrome('C:/section3/webdriver/chrome/chromedriver.exe')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3) # 암묵적으로 5초간 기다림(아무것도 오지 않았는데 실행 되면 안되므로)
driver.get('https://www.inflearn.com/signup')
time.sleep(7)
driver.implicitly_wait(7)

driver.find_element_by_xpath('//*[@id="header"]/nav/div[2]/div/div[2]/div[2]/div[2]/a[1]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/article/form/div/input').send_keys('seongjae6751@naver.com')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/article/form/div/div/input').send_keys('rlatjdwo1303@')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="root"]/div[4]/article/form/button').click()

