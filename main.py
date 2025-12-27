import re
import mss
import time
import mss.tools
import pyautogui
import pytesseract
from PIL import Image
from win11toast import toast

playerNumberScreenshotCoords = {
    "top": 328,
    "left": 1807,
    "width": 50,
    "height": 30
}

while True:
    with mss.mss() as sct:
        sct_img = sct.grab(playerNumberScreenshotCoords)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="playerNumber.png")

        fullPlayerNumber = pytesseract.image_to_string(
            Image.open("playerNumber.png"),
            config="--psm 7"
        )

        match = re.search(r"(\d+)\s*/\s*(\d+)", fullPlayerNumber)
        if not match:
            time.sleep(1)
            continue

        shortenPlayerNumber = int(match.group(1))

        if shortenPlayerNumber < 8:
            pyautogui.moveTo(1190, 337)
            pyautogui.click()
            toast(
                "Auto Minecraft Bedrock Friend World Joiner",
                "Slot frei! Betrete Welt..."
            )

    time.sleep(1)
