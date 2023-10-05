import pyautogui
from time import sleep
n=int(input())
x=1
sleep(5)
for i in range(0,n):
    for j in range(0,x):
        pyautogui.write('#',interval=0.25)
    pyautogui.press('enter')
    x+=1
# import pyautogui

# t=int(input())
# for i in range(1,t+1):   
#     pyautogui.write('#'*i)
#     pyautogui.press('enter')
