import pyautogui
from time import sleep
import random

def excluirLance():
    for x in range(50):
        pyautogui.click(1580,682)
        pyautogui.click(1020,403)
        print(x)
        sleep(1)
        

def lanceGol():
    #lances = [290,315,340,365,390,415,440,465,490,510]
    time = [1705,1825]
    titular = [359,379,401,419,443,464,482,505,525,547,569]
    for x in range(10):
        equipe = random.choice(time)
        #lance = random.choice(lances)
        #lance = [440,290,440,290,315,290,315]
        titulares = random.choice(titular)
        pyautogui.click(228,330)
        pyautogui.write('Lance de gol!')
        pyautogui.click(1533,340)
        pyautogui.click(equipe,titulares)
        pyautogui.click(1386,520)
        sleep(1)
        pyautogui.click(952,403)
        sleep(2)

#lanceGol()
excluirLance()
