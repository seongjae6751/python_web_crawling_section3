from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options
driver = webdriver.Chrome('C:/section3/webdriver/chrome/chromedriver.exe')
driver.get('https://www.koreatech.ac.kr/kor/Main.do')
driver.implicitly_wait(7)
driver.find_element_by_xpath('//*[@id="tmn6"]/a').click()
driver.implicitly_wait(7)
driver.quit()