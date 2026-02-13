

from Classes.SuperClass import SuperClass
from .Button import Button
from .Image import Image


class ImageButton(SuperClass):
    def __init__(self, Pos, Size, BackgroundColor, ImagePath, zIndex=1):
        super().__init__("Textbox", ["Image", "Button", "TypingIn"], [])
        self.Image = Image(Pos, Size, BackgroundColor, ImagePath, zIndex+1)
        self.Button = Button(Pos, Size, BackgroundColor, zIndex)

        self.MouseDown = self.Button.MouseDown
        self.MouseUp = self.Button.MouseUp
        self.MouseClickOff = self.Button.MouseClickOff

    def refresh(self, screen):
        self.Image.refresh(screen)
        self.Button.refresh(screen)
