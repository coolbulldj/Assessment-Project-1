import pygame as py
from Classes.GUIClasses.GUIBase import GetGuiAssets

py.init()

ASPECT_RATIO = 16 / 9
BACKGROUND_COLOR = (0, 0, 255)

screen = py.display.set_mode((800, 450), py.RESIZABLE)

running = True


def TickDisplay():
    global screen
    screen.fill((BACKGROUND_COLOR))

    UIAssets = GetGuiAssets()
    for guiObject in UIAssets:
        guiObject.refresh(screen)
    # rectDetails = py.Rect(0, 0, 100, 100xde)
    # py.draw.rect(screen, (0, 255, 0), rectDetails, 0)
    py.display.update()
