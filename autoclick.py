import pyautogui
import random
import sys


def screen_dimensions():
    screen_size = pyautogui.size()
    new_height = screen_size.height - 10
    new_width = screen_size.width - 10
    return new_height, new_width


def random_movement(max_h, max_w):
    y_val = random.randint(10, max_h)
    x_val = random.randint(10, max_w)
    pyautogui.moveTo(x_val, y_val, 2, pyautogui.easeOutQuad)
    print(pyautogui.position())


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5
interval = 0.5
session = True

prompt_choice = pyautogui.confirm(text='Select which corner to click\n(end by moving your mouse to any corner of the '
                                       'screen)', title='Auto-clicker', buttons=['LEFT', 'NO-CLICK', 'RIGHT'])

try:
    if prompt_choice == 'LEFT':
        max_height, max_width = screen_dimensions()
        while session:
            random_movement(max_height, max_width)
            pyautogui.moveTo(10, 10, 2, pyautogui.easeOutQuad)
            pyautogui.click(x=10, y=10, clicks=1, interval=interval, button='left')

    if prompt_choice == 'RIGHT':
        max_height, max_width = screen_dimensions()
        while session:
            random_movement(max_height, max_width)
            pyautogui.moveTo(max_width, 10, 2, pyautogui.easeOutQuad)
            pyautogui.click(x=max_width, y=10, clicks=1, interval=interval, button='left')

    if prompt_choice == 'NO-CLICK':
        max_height, max_width = screen_dimensions()
        while session:
            random_movement(max_height, max_width)

except pyautogui.FailSafeException as e:
    pyautogui.alert("Completed Script - Fail-safe")
    sys.exit()
except KeyboardInterrupt:
    pyautogui.alert("Completed Script - Keyboard Interrupt")
    sys.exit()

sys.exit()
