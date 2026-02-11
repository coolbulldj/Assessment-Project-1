from .Connection import Connection
from GeneralFunctions import CreateUniqueKeyForMap


class Event:
    def __init__(self):
        self.cbs = {}

    def _FireEvent(self, *args):
        for cb in self.cbs.values():
            cb(*args)

    def Once(self, cb):
        key = CreateUniqueKeyForMap(self.cbs)

        def DisconnectCB():
            self.cbs[key] = None

        def Onevent(*args):
            DisconnectCB()
            cb(*args)

        self.cbs[key] = Onevent

        EventConnection = Connection(DisconnectCB)

        return EventConnection

    def Connect(self, cb):
        key = CreateUniqueKeyForMap(self.cbs)

        def DisconnectCB():
            self.cbs[key] = None

        self.cbs[key] = cb

        EventConnection = Connection(DisconnectCB)

        return EventConnection

    def Wait(self, _):
        key = CreateUniqueKeyForMap(self.cbs)

        def DisconnectCB():
            self.cbs[key] = None

        self.cbs[key] = "Wating..."

        while self.cbs[key]:
            print("wating")
            pass
