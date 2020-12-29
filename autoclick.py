import pyautogui
import random
import sys

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
interval = 0.5
session = True

prompt_choice = pyautogui.confirm(text='Select which corner to click', title='Auto-clicker', buttons=['LEFT', 'RIGHT'])
screen_size = pyautogui.size()

try:
    if prompt_choice == 'LEFT':
        while session:
            y = random.randint(0, screen_size.height)
            x = random.randint(0, screen_size.width)
            pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
            print(pyautogui.position())
            pyautogui.moveTo(10, 10, 2, pyautogui.easeOutQuad)
            pyautogui.click(x=10, y=10, clicks=1, interval=interval, button='left')

    if prompt_choice == 'RIGHT':
        while session:
            y = random.randint(0, screen_size.height)
            x = random.randint(0, screen_size.width)
            pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
            print(pyautogui.position())
            pyautogui.moveTo(screen_size.width - 10, 10, 2, pyautogui.easeOutQuad)
            pyautogui.click(x=screen_size.width - 10, y=10, clicks=1, interval=interval, button='left')

except pyautogui.FailSafeException as e:
    pyautogui.alert("Completed Script - Fail-safe")
    sys.exit()
except KeyboardInterrupt:
    pyautogui.alert("Completed Script - Keyboard Interrupt")
    sys.exit()

sys.exit()  # pyinstaller --onefile autoclick.py
