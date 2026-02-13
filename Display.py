import pygame as py
from Classes.GUIClasses.GUIBase import GetGuiAssets
from Classes.GUIClasses.Button import getButtonList

py.init()

ASPECT_RATIO = 16/9
BACKGROUND_COLOR = (0, 0, 255)

screen = py.display.set_mode((200, 112.5), py.RESIZABLE)

running = True

def TickDisplay(dt:int):
    global screen
    for event in py.event.get():
        bList = getButtonList()

        if event.type == py.MOUSEBUTTONDOWN:
            for clickCB in bList["MouseDown"]:
                clickCB(screen, event.pos)
        elif event.type == py.MOUSEBUTTONUP:
            for clickCB in bList["MouseUp"]:
                clickCB(screen, event.pos)

        if event.type == py.VIDEORESIZE:
            new_width = event.w
            new_height = int(new_width / ASPECT_RATIO)

            # If height is too large for what user dragged,
            # base it on height instead
            if new_height > event.h:
                new_height = event.h
                new_width = int(new_height * ASPECT_RATIO)

            screen = py.display.set_mode(
                (new_width, new_height),
                py.RESIZABLE
            )

    screen.fill((BACKGROUND_COLOR))

    UIAssets = GetGuiAssets()
    for guiObject in UIAssets:
        guiObject.refresh(screen)
    # rectDetails = py.Rect(0, 0, 100, 100xde)
    # py.draw.rect(screen, (0, 255, 0), rectDetails, 0)
    py.display.update()
