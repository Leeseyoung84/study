import pyautogui

i=pyautogui.locateCenterOnScreen('7.png') 
#센터값을 바로구함

pyautogui.click(i)
#구한 값을 클릭
print(i)

