import pygame as py
from Classes.GUIClasses.GUIBase import GUIBase


screen = py.display.set_mode((200, 200), py.RESIZABLE)

guiObject = GUIBase((0.5, 0.5), (0.25, 0.25), (255,0, 0))

running = True

while running:
    for event in py.event.get():  # ← looping through inputs
        if event.type == py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            print("Key pressed:", event.key)

        if event.type == py.MOUSEBUTTONDOWN:
            print("Mouse clicked:", event.pos)
   #screen.fill((255,255,255))
    guiObject.refresh(screen)
    #rectDetails = py.Rect(0, 0, 100, 100)
    #py.draw.rect(screen, (0, 255, 0), rectDetails, 0)
    py.display.flip()