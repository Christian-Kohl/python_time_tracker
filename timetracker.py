# Actual class to keep track of the time spent on the computer, it will take note of an individual application, or a specific website.


def main():
    return

# Method to keep track of the time, and increment each few seconds, to see what exactly the computer is focussed on


def get_active_window_raw():
    '''
    returns the details about the window not just the title
    '''
    root = subprocess.Popen(
        ['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
    stdout, stderr = root.communicate()

    m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
    if m != None:
        window_id = m.group(1)
        window = subprocess.Popen(
            ['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE)
        stdout, stderr = window.communicate()
    else:
        return None

    match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match != None:
        ret = match.group("name").strip(b'"')
        # print(type(ret))
        '''
        ret is str for python2
        ret is bytes for python3 (- gives error while calling in other file)
        be careful
        '''
        return ret
    return None

# Method to identify what application is being used by the user at this specific time

# Methods to check Google Chrome, or Firefox to identify what tab is open.
