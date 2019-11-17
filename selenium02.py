from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()

#time.sleep(10)
driver.implicitly_wait(10)
driver.get('https://naver.com')

#단순히 버튼 아이디를 찾아서 클릭하는소스
#button= driver.find_element_by_css_selector('#search_btn')
#그러나 버튼의 css를 가져오는데까지 10초를 기다린다음 누름 
button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#search.btn')))
button.click()