import pygame as py
import sys
import time
#Classes
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.ImageButton import ImageButton

#Services / Modules
from Services.InputService import FireKeyPress, FireKeyRelease
from Display import TickDisplay



py.init()

# guiObject = TextLabel(
#     (0.5, 0.5), (0.25, 0.25), (255, 0, 255, 0), (111, 111, 111), "SF Pro", 1, 2
# )

# guiObject.Text = "$"

BackgroundImage = Image(
    (0.5, 0.375), (0.75, 0.75), (200, 200, 0, 0), "Assets\MartianBackground.png", zIndex=2
)

Status = Image(
    (0.5, 0.5), (1, 1), (200, 200, 0, 0), "Assets\MetalTexture.jpg", zIndex=1
)

NextTermButton = ImageButton(
    (0.5, 0.5), (0.25, 0.25), (200, 200, 0, 0), r"Assets\NextTermB.png", zIndex=1
)



#0.875

StartTime = time.time()
LastFrameTime= time.time()

ElapedTime = 0

running = True

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            running = False

        if event.type == py.KEYDOWN:
            FireKeyPress(event.key)
            #print("Key pressed:", event.key)
        if event.type == py.KEYUP:
            FireKeyRelease(event.key)
            #print("Key released:", event.key)

    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    TickDisplay(dt)
    #print(dt, ElapedTime)
    LastFrameTime = currentTime
