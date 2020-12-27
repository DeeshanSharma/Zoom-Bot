'''
Author: Deeshan Sharma
Date Created: December 27, 2020
Purpose: This is a bot which will join the zoom meetings on your behalf automatically and mark your attendance.
'''

import json
from datetime import datetime as dt
import subprocess
import time

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
        else:
            time.sleep(240)

def openZoom():
    subprocess.Popen(r"C:\Users\princ\AppData\Roaming\Zoom\bin\Zoom.exe")
    time.sleep(20)

timetable = getTime()
checkClass(timetable)