from Classes.SuperClass import SuperClass
from .Button import Button
from .Image import Image


class ImageButton(SuperClass):
    def __init__(
        self, Pos, Size, BackgroundColor, BackgroundTranspareny, ImagePath, zIndex=1
    ):
        super().__init__(
            "ImageButton",
            ["Image", "Button", "TypingIn", "MouseDown", "MouseUp", "MouseClickOff", "Visible"],
            ["Visible"],
        )
        self.Visible = True
        self.Image = Image(
            Pos, Size, BackgroundColor, BackgroundTranspareny, ImagePath, zIndex + 1
        )
        self.Button = Button(Pos, Size, BackgroundColor, BackgroundTranspareny, zIndex)

        self.MouseDown = self.Button.MouseDown
        self.MouseUp = self.Button.MouseUp
        self.MouseClickOff = self.Button.MouseClickOff

        def UpdateVisiblity(newVisiblity):
            self.Image.Visible = newVisiblity
            self.Button.Visible = newVisiblity
        
        self.GetPropertyChangedSignal("Visible", UpdateVisiblity)
