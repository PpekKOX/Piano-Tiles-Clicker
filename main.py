import pyautogui as pg
from time import sleep
import keyboard
import  win32api, win32con


# Define a key to close the script
def close_script():
    if keyboard.is_pressed('esc'):
        print('Script turned OFF')
        return True
    return False

# Define the mouse left-clicking function
def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Wait 3 seconds before entering the script
sleep(3)

# Script that looks for pixel colors to match the piano-tile colors
with open('pianotiles_data.txt', 'w') as t1:
    while True:
        if close_script():
            break
        if pg.pixel(603,503) [0] == 0:
            click(603,503)
            t1.write('Clicked 1st Tile!\n')
        elif pg.pixel(679,502) [0] == 0:
            click(679,502)
            t1.write('Clicked 2nd Tile!\n')
        elif pg.pixel(773,506) [0] == 0:
            click(773,506)
            t1.write('Clicked 3rd Tile!\n')
        elif pg.pixel(860,507) [0] == 0:
            click(860,507)
            t1.write('Clicked 4th Tile!\n')

# Link for the game: https://www.agame.com/game/magic-piano-tiles
