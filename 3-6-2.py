from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless") #CLI(백엔드로 작동)

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:/section3/webdriver/chrome/chromedriver.exe')
# driver.set_window_size(1920,1280)
# driver.implicitly_wait(5) # 암묵적으로 5초간 기다림(아무것도 오지 않았는데 실행 되면 안되므로)

driver.get('https://google.com')
# time.sleep(5)

driver.save_screenshot("c:/website1_ch.png")

# driver.implicitly_wait(5)

driver.get('https://www.daum.net')
# time.sleep(5)

driver.save_screenshot("c:/website2_ch.png")

driver.quit() # driver 종료

print('스크린샷 완료')