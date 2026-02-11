class Connection:
    def __init__(self, disconnectMethod):
        self.DisconnectMethod = disconnectMethod
        self.Connected = True

    def Disconnect(self):
        if not self.Connected:
            return
        self.Connected = False
        self.DisconnectMethod()
