import pygame as py
import sys
from Classes.GUIClasses.TextLabel import TextLabel

py.init()

screen = py.display.set_mode((200, 200), py.RESIZABLE)

guiObject = TextLabel((0.5,0.5), (0.25,0.25), (255,0,255), (111, 111, 111))

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
    # screen.fill((255,255,255))
    guiObject.refresh(screen)
    # rectDetails = py.Rect(0, 0, 100, 100)
    # py.draw.rect(screen, (0, 255, 0), rectDetails, 0)
    py.display.flip()
