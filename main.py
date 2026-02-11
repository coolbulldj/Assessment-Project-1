import time

from Classes.EventClass import Event



ranconnet = Event()

ranconnet.Once(lambda: print("hello world"))

time.sleep(3)

ranconnet._FireEvent()