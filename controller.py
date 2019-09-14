from datetime import datetime
import time
import os
from timetracker import *

'''
Main class, to take in the user's commands, and the different flags/conditions. This will then use this to fetch the wanted information, or to keep track of time.
'''
starttime = None


def tracker():
    folder = "track_logs"
    starttime = datetime.now().strftime('%d-%m-%Y')
    current_data = None
    while True:
        new_data = main_track()
        if new_data != current_data:
            current_activity
        time.sleep(5)


try:
    tracker()
except KeyboardInterrupt:
    print('That\'s a shame :(')
