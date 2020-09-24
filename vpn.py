import pyautogui
from time import sleep

def login():
    pyautogui.click(541,311)
    pyautogui.write('sudo openconnect https://portalssl.rbs.com.br')
    pyautogui.press('enter')
    sleep(2)

    pyautogui.write('Patric1@1')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write('tc-geibson_barbosa')
    pyautogui.press('enter')
    sleep(2)    
    pyautogui.write('Patric1@3')
    pyautogui.press('enter')
    sleep(2)


    pyautogui.write('sudo openconnect https://portalssl.rbs.com.br')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write('tc-geibson_barbosa')
    pyautogui.press('enter')
    sleep(2)    
    pyautogui.write('Patric1@3')
    pyautogui.press('enter')
    sleep(2)
 

login()
