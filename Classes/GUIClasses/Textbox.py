from Classes.SuperClass import SuperClass
from .Button import Button
from .TextLabel import TextLabel
from Services.InputService import InputPress

def is_valid_chr(n):
    return isinstance(n, int) and 0 <= n <= 0x10FFFF


class Textbox(SuperClass):
    def __init__(self, Pos, Size, BackgroundColor, TextColor, TextFont, zIndex=1):
        super().__init__("Textbox", ["Textlabel", "Button", "TypingIn"], [])
        self.Textlabel = TextLabel(Pos, Size, BackgroundColor, TextColor, TextFont, 1, zIndex+1)
        self.Button = Button(Pos, Size, BackgroundColor, zIndex)
        self.TypingIn = False

        self.Button.MouseClickOff.Connect(self.stop_typing)
        self.Button.MouseUp.Connect(self.start_typing)
        InputPress.Connect(self.typing)

    def typing(self, keycode):
        
        if not is_valid_chr(keycode):
            #keycode is not able to be translated to a string therefore remove it
            
            return

        if not self.TypingIn:
            return
        
        if keycode == 8:
            self.Textlabel.Text = self.Textlabel.Text[:-1]
            return
 
        self.Textlabel.Text += chr(keycode)

    def stop_typing(self):
        self.TypingIn = False

    def start_typing(self):
        self.Textlabel.Text = ""
        self.TypingIn = True

    def refresh(self, screen):
        self.Textlabel.refresh(screen)
        self.Button.refresh(screen)
