from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options()
firefox_options.add_argument("--headless") #CLI(백엔드로 작동)

driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='C:/section3/webdriver/firefox/geckodriver.exe')
# driver.set_window_size(1920,1280)
# driver.implicitly_wait(5) # 암묵적으로 5초간 기다림(아무것도 오지 않았는데 실행 되면 안되므로)

driver.get('https://google.com')
# time.sleep(5)

driver.save_screenshot("c:/website1_ff.png")

# driver.implicitly_wait(5)

driver.get('https://www.daum.net')
# time.sleep(5)

driver.save_screenshot("c:/website2_ff.png")

driver.quit() # driver 종료

print('스크린샷 완료')