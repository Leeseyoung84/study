from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()

#time.sleep(10)
driver.implicitly_wait(10)
driver.get('https://naver.com')


#button= driver.find_element_by_css_selector('#search_btn')

button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#search.btn')))
button.click()