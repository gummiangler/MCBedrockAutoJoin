import os
import time
import pyautogui

while True:
    try:
        world = pyautogui.locateCenterOnScreen("images/world.png", confidence=0.9)
        print("Welt gefunden!")
    except pyautogui.ImageNotFoundException:
        world = None
        print("Welt nicht gefunden!")

    if world is not None:
        try:
            pyautogui.locateCenterOnScreen("images/players.png", confidence=0.9)
            print("Kein Platz auf der Welt frei!")
        except pyautogui.ImageNotFoundException:
            print("Platz frei!")
            pyautogui.click(world)
            os.system('kdialog --title "MCBedrockAutoJoin" --warningcontinuecancel "Slot frei!"')

    print("")
    time.sleep(2)
