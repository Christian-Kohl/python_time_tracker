class Windowobject:

    title = None
    tab = None
    data = None
    starttime = None
    endtime = None
    totaltime = None

    def __init__(self, title, tab, starttime):
        self.starttime = starttime
        self.title = title
        self.tab = tab
        return None

    def end_object(self, endtime):
        self.endtime = endtime
        self.totaltime = endtime - starttime
