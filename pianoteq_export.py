from time import sleep
import pyautogui

sleep(3)

while True:
    # open dialog
    pyautogui.hotkey("command", "o", interval=1)

    # select next hymnary
    pyautogui.press("down", interval=0.5)
    pyautogui.press("enter")

    # export
    pyautogui.hotkey("command", "e", interval=0.5)
    pyautogui.press(["\t"] * 7)
    pyautogui.press("enter")

    while pyautogui.locateOnScreen("pianoteq.png") is None:
        sleep(1)
        print("waiting export")
