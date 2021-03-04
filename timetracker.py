import os
import time
import schedule
from datetime import datetime


def track():
    currentProc = os.system("ps -e | grep $(xdotool getwindowpid "
                            "$(xdotool getwindowfocus)) | grep -v grep |"
                            "awk '{print $4}'")
    currentWin = os.system("xdotool getwindowfocus getwindowname")
    currentTime = datetime.now()
    print(currentTime, "\n", currentProc, "\n", currentWin)


if __name__ == "__main__":
    schedule.every(2).minutes.do(track)
    while 1:
        schedule.run_pending()
        time.sleep(1)
