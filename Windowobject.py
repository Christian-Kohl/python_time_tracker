class Windowobject:

    title = None
    tab = None
    data = None
    starttime = None
    endtime = None
    totaltime = None

    def __init__(self, title, tab, data, starttime):
        self.starttime = starttime
        self.title = title
        self.tab = tab
        self.data = data
        return None

    def end_object(self, endtime):
        self.endtime = endtime
        self.totaltime = self.endtime - self.starttime

    def update_website_entity(self):
        if self.title in ['chrome', 'firefox']:
            tab_info = self.tab.split(' - ')
            if tab_info[-1] in ['Netflix', 'YouTube', 'Facebook', 'Instagram']:
                self.title = tab_info[-1]
            elif 'reddit' in self.title:
                self.title = 'Reddit'
