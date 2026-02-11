from .EventClass import Event


class SuperClass():

    def __init__(self, ClassName, ValidProperties, SignalProperties):
        self.ClassName = ClassName
        self._Events = {} #The Events from Get Property Changed Signal { [propertyName] = EventObject }
        self.ValidProperties = ValidProperties
        self.SignalProperties = SignalProperties
        self._initialized = True

    def __setattr__(self, name, value):
        initialized = hasattr(self, "_initialized")

        if not initialized:
            super().__setattr__(name, value)
            return

        if not hasattr(self, name) and name not in self.ValidProperties:
            print(f"WARNING: The Property:{name} is not a valid property of Class:{self.ClassName}")

    def GetPropertyChangedSignal(self, property:str):
        if property not in self.SignalProperties:
            print(f"WARNING: GetPropertyChangedSignal Cannot return a event for property:{property} as this property is not a valid signal property")
            return
        PropertyEvent = None
        if property not in self._Events:
            PropertyEvent = Event()
            self._Events[property] = PropertyEvent
        else:
            PropertyEvent = self._Events[property]

        return PropertyEvent