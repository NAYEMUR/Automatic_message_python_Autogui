import pyautogui
import time
sms=0
while sms < 500:
    time.sleep(1)
    pyautogui.typewrite("Hello ! HOW ARE YOU")
    pyautogui.press('enter')
    sms=sms+1