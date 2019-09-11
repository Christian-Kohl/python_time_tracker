from datetime import datetime
import os

'''
Main class, to take in the user's commands, and the different flags/conditions. This will then use this to fetch the wanted information, or to keep track of time.
'''


def tracker():
    folder = "track_logs"
    date = datetime.now().strftime('%d-%m-%Y')


tracker()
