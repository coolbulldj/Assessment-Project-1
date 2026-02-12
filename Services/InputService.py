from Classes.EventClass import Event

InputPress = Event()
InputRelease = Event()
#Later events
#InputHeld
#InputDoubleTap

def FireKeyPress(key):
    InputPress._FireEvent(key)

def FireKeyRelease(key):
    InputRelease._FireEvent(key)