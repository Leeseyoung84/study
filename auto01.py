from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

#chrome으로 웹사이트를 열었다
driver = webdriver.Chrome()

url='https://google.com'
driver.get(url)
driver.maximize_window()    #창을 제일 크게 열음
#driver변수에 크롬브라우져로 구글을 열고 액션 변수에 넣음 
action = ActionChains(driver)

#구글페이지의 id를 가져옴 id니까 #을 넣고 클릭
driver.find_element_by_css_selector('#gb_70').click()

#아이디를 입력하는 방법  #꼭 perform을 꼭 넣어야함
action.send_keys('kobv4278').perform()    

#로그인버튼의 검사해서 클래스파일이므로.클래스명으로 변수를 넣고 클릭하게함
driver.find_element_by_css_selector('.CwaK9').click()


action.reset_actions()

time.sleep(1)

#비밀번호 넣는법  비밀번호 창 검색후 클래스 이름을 넣어주고 버튼 누름
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('tlscjs2726')
driver.find_element_by_css_selector('.CwaK9').click()

time.sleep(2)



#gmail로 들어가는데 gmail화면의 주소를 복사하고 driver.get을 함
driver.get('https://mail.google.com/mail/u/0/?ogbl#inbox')
time.sleep(1)

#편지쓰기 버튼 누르기 
#편지쓰기 오른쪽버튼 검사후, class파일 복사 빈공간은 .으로 채워줌
driver.find_element_by_css_selector('.T-I.J-J5-Ji.T-I-KE.L3').click()
time.sleep(1)





send_button=driver.find_element_by_css_selector('.gU.Up')

action.reset_actions()

(
action.send_keys('kobv4278@gmail.com').pause(2).key_down(Keys.ENTER)
.key_down(Keys.TAB).key_down(Keys.TAB)
.send_keys('제목입니다').pause(2).key_down(Keys.TAB)
.send_keys('abcde').pause(2).key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcde').key_down(Keys.SHIFT)
.move_to_element(send_button).click()
.perform()
)


