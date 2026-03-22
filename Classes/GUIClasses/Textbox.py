from Classes.SuperClass import SuperClass
from .Button import Button
from .TextLabel import TextLabel
from Services.InputService import InputPress


def is_valid_chr(n):
    return isinstance(n, int) and 0 <= n <= 0x10FFFF


class Textbox(SuperClass):
    def __init__(
        self,
        Pos,
        Size,
        BackgroundColor,
        BackgroundTranspareny,
        TextColor,
        TextFont=1,
        zIndex=1,
    ):
        super().__init__("Textbox", ["Textlabel", "Button", "TypingIn", "Visible"], ["Visible"])
        self.Textlabel = TextLabel(
            Pos,
            Size,
            BackgroundColor,
            BackgroundTranspareny,
            TextColor,
            TextFont,
            1,
            zIndex + 1,
        )
        B = Button(Pos, Size, BackgroundColor, zIndex)
        self.TypingIn = False
        self.Visible = True

        B.MouseClickOff.Connect(self.stop_typing)
        B.MouseUp.Connect(self.start_typing)
        InputPress.Connect(self.typing)

        self.Button = B

        def UpdateVisiblity(newVisiblity):
            self.Textlabel.Visible = newVisiblity
            self.Button.Visible = newVisiblity
        
        self.GetPropertyChangedSignal("Visible").Connect(UpdateVisiblity)

    def typing(self, keycode):
        if not is_valid_chr(keycode):
            # keycode is not able to be translated to a string therefore remove it

            return

        if not self.TypingIn:
            return

        if keycode == 8:
            self.Textlabel.Text = self.Textlabel.Text[:-1]
            return
        SetText = self.Textlabel.Text + chr(keycode)
        self.Textlabel.Text = SetText

    def stop_typing(self):
        self.TypingIn = False

    def start_typing(self):
        #print("start_typing")
        self.Textlabel.Text = ""
        self.TypingIn = True
