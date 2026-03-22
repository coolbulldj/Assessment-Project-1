from Classes.SuperClass import SuperClass
from .Button import Button
from .TextLabel import TextLabel


class TextButton(SuperClass):
    def __init__(
        self,
        Pos,
        Size,
        BackgroundColor,
        BackgroundTranspareny,
        TextColor,
        TextFont="monospace",
        TextSize=1,
        zIndex=1,
        UIAspectRatio=None,
        TextScaled=True,
    ):
        super().__init__(
            "TextButton",
            [
                "TextLabel",
                "Button",
                "TypingIn",
                "Text",
                "MouseDown",
                "MouseUp",
                "MouseClickOff",
                "Visible"
            ],
            ["Text", "Visible"],
        )
        self.TextLabel = TextLabel(
            Pos,
            Size,
            BackgroundColor,
            BackgroundTranspareny,
            TextColor,
            TextFont,
            TextSize,
            zIndex,
            UIAspectRatio,
            TextScaled,
        )

        self.Text = ""
        self.Visible = True

        def UpdateVisiblity(newVisiblity):
            self.TextLabel.Visible = newVisiblity
            self.Button.Visible = newVisiblity
        
        self.GetPropertyChangedSignal("Visible").Connect(UpdateVisiblity)

        def update_text(a):
            self.TextLabel.Text = a

        self.GetPropertyChangedSignal("Text").Connect(update_text)

        self.Button = Button(Pos, Size, BackgroundColor, 1, zIndex)

        self.MouseDown = self.Button.MouseDown
        self.MouseUp = self.Button.MouseUp
        self.MouseClickOff = self.Button.MouseClickOff
