import pyautogui,time,win32api,win32con
from time import sleep


#https://pyautogui.readthedocs.io/en/latest/quickstart.html#mouse-functions

start_point = "https://www.google.com/maps/@40.7577264,-73.9849788,3a,75y,300.05h,101.55t/data=!3m6!1e1!3m4!1sz2oHW5ENbupBF1hquoEqYg!2e0!7i16384!8i8192?entry=ttu"

def movement(direction,seconds):
    if direction.lower() == 'left':
        key_code = win32con.VK_LEFT
    elif direction.lower() == 'right':
        key_code = win32con.VK_RIGHT

    start = time.time()
    while time.time() - start < seconds:
        win32api.keybd_event(key_code, 0, 0, 0)
    #release the key    
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    
def move_around(seconds):
    #activate the screen by rightclick
    pyautogui.click(466,629, button='right')
    movement('left',seconds)
    sleep(0.5)
    movement('right',seconds)
    sleep(0.2)
    movement('right',seconds)
    sleep(0.5)
    movement('left',seconds)

def move_forward(steps,waiting_time):
    for i in range(steps):
        pyautogui.hotkey('up')
        sleep(waiting_time)

def run():
    #to activate the windows
    pyautogui.click(466,629, button='right')

    move_forward(2,4)
    move_around(1)
    sleep(3)
    move_forward(3,4)
    move_around(1.5)
    sleep(3)
    movement('left',1.2)
    sleep(5)
    pyautogui.click(450,764)
    sleep(4)
    move_around(1.5)
    sleep(2)
    move_forward(2,4)
    move_around(1)
    sleep(3)
    move_forward(4,4)
    move_around(2)
