import subprocess
import time
import schedule
from datetime import datetime
import dbManager
import itertools


def track():
    currentProc = subprocess.check_output(
            "ps -e | grep $(xdotool getwindowpid "
            "$(xdotool getwindowfocus)) | grep -v grep |"
            "awk '{print $4}'", shell=True
            ).decode("utf-8").rstrip()
    currentWin = subprocess.check_output(
            "xdotool getwindowfocus getwindowname", shell=True
            ).decode("utf-8").rstrip()
    currentTime = datetime.now()
    dbManager.insertEntry(currentProc, currentWin)
    print(currentTime)


def updateHistory():
    data = dbManager.getPreviousData()
    groups = itertools.groupby(
                data, key=lambda x: x["time"].date()
                )
    for i in groups:
        if i[0] < datetime.datetime.now().date():
            createDayEntry(i[0], i[1])
        for j in i[1]:
            print(j)


def createDayEntry(date, entries):
    entryList = []
    for entry in entries:
        entryList += [entry]


if __name__ == "__main__":
    updateHistory()
    schedule.every(2).minutes.do(track)

    track()
    while 1:
        schedule.run_pending()
        time.sleep(1)
