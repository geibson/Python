import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        posi = pyautogui.position()
        print('clicou '+posi)
        
with Listener(on_click=on_click, on_press=on_press) as listener:
    listener.join()
