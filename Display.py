import pygame as py
import sys
from Classes.GUIClasses.GUIBase import GetGuiAssets
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Image import Image

py.init()

ASPECT_RATIO = 16/9
BACKGROUND_COLOR = (100, 100, 100)

screen = py.display.set_mode((200, 112.5), py.RESIZABLE)

guiObject = TextLabel(
    (0.5, 0.5), (0.25, 0.25), (255, 0, 255), (111, 111, 111), "SF Pro", 1, 2
)

guiObject.Text = "🥰"
ImageLabel = Image(
    (0.5, 0.5), (0.5, 0.5), (200, 200, 0), "Assets\MartianBackground.png"
)

running = True

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            running = False

        if event.type == py.KEYDOWN:
            print("Key pressed:", event.key)

        if event.type == py.MOUSEBUTTONDOWN:
            print("Mouse clicked:", event.pos)

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
    py.display.flip()
