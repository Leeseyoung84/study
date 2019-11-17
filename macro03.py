#바로 스크린에서 캡쳐해서 그화면을 클릭하는 프로그램

import pyautogui

#한쪽끝을 알아내서 가로세로 네모를 만들므로
#커서가 있는 곳의 좌표를 알아내기(93,819)
print(pyautogui.position())

#1이라는 이름으로 스크린샷 하기
pyautogui.screenshot('1.png',region=(69,788,97,101))
#같은 폴더에 1이라는 스크린 샷이 생김

#1.png캡쳐파일의센터값을 알아내서 num1 에 넣음
num1= pyautogui.locateCenterOnScreen('1.png')
#num1값을 클릭
pyautogui.click(num1)