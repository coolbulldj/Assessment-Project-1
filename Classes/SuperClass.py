from .EventClass import Event
# import traceback


class SuperClass:
    def __init__(self, ClassName, ValidProperties, SignalProperties):
        self.ClassName = ClassName
        self.Name = ClassName
        self._Events = {}  # The Events from Get Property Changed Signal { [propertyName] = EventObject }
        self.ValidProperties = ValidProperties  # array
        self.SignalProperties = SignalProperties  # array
        self._initialized = True

    def __setattr__(self, name, value):
        # if name == "Text":
        #         # print(" ")
        #         # print("new text",value)
        #         # traceback.print_stack()
        #         # print(" ")
        initialized = hasattr(self, "_initialized")

        if not initialized:
            super().__setattr__(name, value)
            return

        if not hasattr(self, name) and name not in self.ValidProperties:
            print(
                f"WARNING: The Property:{name} is not a valid property of Class:{self.ClassName}"
            )

        super().__setattr__(name, value)

        if name in self._Events.keys():
            # print(self._Events, self.SignalProperties, name)
            SignalEvent = self._Events[name]
            SignalEvent._FireEvent(value)

    def GetPropertyChangedSignal(self, property: str):
        if property not in self.SignalProperties:
            print(
                f"WARNING: GetPropertyChangedSignal Cannot return a event for property:{property} as this property is not a valid signal property"
            )
            return
        PropertyEvent = None
        if property not in self._Events:
            PropertyEvent = Event()
            self._Events[property] = PropertyEvent
        else:
            PropertyEvent = self._Events[property]

        return PropertyEvent
