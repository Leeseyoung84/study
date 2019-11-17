from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome()
url='https://google.com'
driver.get(url)


#input테그의 클래스명
#gLFyf gsfi


driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys("파이썬")
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

