import os
import time
import schedule
from datetime import datetime
import dbManager


def track():
    currentProc = os.system("ps -e | grep $(xdotool getwindowpid "
                            "$(xdotool getwindowfocus)) | grep -v grep |"
                            "awk '{print $4}'")
    currentWin = os.system("xdotool getwindowfocus getwindowname")
    currentTime = datetime.now()
    dbManager.insertEntry(currentProc, currentWin)
    print(currentTime, "\n", currentProc, "\n", currentWin)


def updateHistory():
    dbManager.getPreviousData()


if __name__ == "__main__":
    updateHistory()
    schedule.every(2).minutes.do(track)

    while 1:
        schedule.run_pending()
        time.sleep(1)
