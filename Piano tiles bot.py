import pyautogui
import keyboard
from time import sleep

sleep(2)

while keyboard.is_pressed('q')==False:

    #Click the start button
    if pyautogui.pixel(670,550)[0]==54:
        pyautogui.click(670,550)
    if pyautogui.pixel(770,550)[0]==54:
        pyautogui.click(770,550)
    if pyautogui.pixel(870,550)[0]==54:
        pyautogui.click(870,550)
    if pyautogui.pixel(970,550)[0]==54:
        pyautogui.click(970,550)

    #Click the black tiles
    if pyautogui.pixel(670,530)[:]==(1,1,1):
        pyautogui.click(670,530)
    if pyautogui.pixel(770,530)[:]==(1,1,1):
        pyautogui.click(770,530)
    if pyautogui.pixel(870,530)[:]==(1,1,1):
        pyautogui.click(870,530)
    if pyautogui.pixel(970,530)[:]==(1,1,1):
        pyautogui.click(970,530)

    #Click the continium tile
    if pyautogui.pixel(670,530)[:]==(0,2,4):
        pyautogui.click(670,530)
    if pyautogui.pixel(770,530)[:]==(0,2,4):
        pyautogui.click(770,530)
    if pyautogui.pixel(870,530)[:]==(0,2,4):
        pyautogui.click(870,530)
    if pyautogui.pixel(970,530)[:]==(0,2,4):
        pyautogui.click(970,530)
    