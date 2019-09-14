from datetime import datetime
import time
import os
from timetracker import *

'''
Main class, to take in the user's commands, and the different flags/conditions. This will then use this to fetch the wanted information, or to keep track of time.
'''
starttime = None
current_list = []


def tracker():
    global current_list
    window = track_current_window()
    current_list += [window]
    while True:
        window = track_current_window()
        window.update_website_entity()
        if not (window.title == current_list[-1].title):
            current_list[-1].end_object(window.starttime)
            current_list += [window]
        time.sleep(1)


try:
    tracker()
except KeyboardInterrupt:
    print('That\'s a shame :(')
    current_list[-1].end_object(datetime.now())
    for x in current_list:
        print(x.title)
        print(x.totaltime)
