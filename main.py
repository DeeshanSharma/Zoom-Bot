"""
Author: Deeshan Sharma
Date Created: December 27, 2020
Purpose: This is a bot which will join the Zoom meetings on your behalf automatically and mark your attendance.
"""

import json
from datetime import datetime as dt
import subprocess
import time
import pyautogui as gui
import link
import getpass

username = getpass.getuser()


def getTime():
    with open('timetable.json', 'r') as f:
        timetable = json.load(f)
    return timetable


def checkClass(timetable):
    day = dt.today().strftime("%A").lower()
    schedule = timetable[day]
    while True:
        cTime = dt.now().strftime("%I:%M")
        if cTime in schedule:
            openZoom()
            time.sleep(240)


def openZoom():
    subprocess.Popen(fr"C:\Users\{username}\AppData\Roaming\Zoom\bin\Zoom.exe")  # Change app location here
    time.sleep(15)
    joinClass()


def buttonClick(image):
    btn = gui.locateCenterOnScreen(image)
    gui.moveTo(btn)
    gui.click()
    time.sleep(2)


def buttonWrite(text):
    gui.write(text)
    time.sleep(1)
    gui.press('enter')


def joinClass():
    buttonClick('images/main-join-btn.png')
    buttonWrite(link.ID)
    time.sleep(6)
    buttonWrite(link.PASS)


timetable = getTime()
checkClass(timetable)
