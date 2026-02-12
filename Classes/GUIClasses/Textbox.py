from Classes.SuperClass import SuperClass
from .Button import Button
from .TextLabel import TextLabel
from Services.InputService import InputPress

class Textbox(SuperClass):
    def __init__(self, Pos, Size, BackgroundColor, TextColor, TextFont):
        super().__init__("Textbox", ["TextLabel", "Button", "TypingIn"], [])
        self.Textlabel = TextLabel(Pos, Size, BackgroundColor, TextColor, TextFont)
        self.Button = Button(Pos, Size, BackgroundColor)
        self.TypingIn = False

        self.Button.MouseClickOff.Connect(self.stop_typing)
        self.Button.MouseUp.Connect(self.start_typing)
        InputPress.Connect(self.typing)

    def typing(self, keycode):
        if self.TypingIn:
            return
        self.Textlabel.Text += chr(keycode)

    def stop_typing(self):
        self.TypingIn = False

    def start_typing(self):
        self.TypingIn = True

    def refresh(self, screen):
        self.Textlabel.refresh(screen)
        self.Button.refresh(screen)
