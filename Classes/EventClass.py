
class Event():
    def __init__(self):
        self.cbs = {}

    def _FireEvent(self, *args):
        for _, cb in self.cbs:
            cb(*args)

    def Once(cb):
        