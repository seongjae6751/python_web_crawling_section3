from selenium import webdriver

driver = webdriver.PhantomJS('C:/section3/webdriver/phantomjs/phantomjs.exe')

driver.implicitly_wait(5) # 암묵적으로 5초간 기다림(아무것도 오지 않았는데 실행 되면 안되므로)

driver.get('https://google.com')

driver.save_screenshot("c:/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')

driver.save_screenshot("c:/website2.png")

driver.quit() # driver 종료

print('스크린샷 완료')






