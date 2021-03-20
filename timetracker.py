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
    dbManager.addToEntry(currentProc, currentWin)
    print(currentTime)


if __name__ == "__main__":
    schedule.every(2).minutes.do(track)

    track()
    while 1:
        schedule.run_pending()
        time.sleep(1)
