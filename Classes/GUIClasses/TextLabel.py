import pygame as py
from .GUIBase import GUIBase


class TextLabel(GUIBase):
    def __init__(
        self, Pos, Size, BackgroundColor, TextColor, zIndex=None, UIAspectRatio=None, TextScaled: bool = True
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            zIndex,
            UIAspectRatio,
            "TextLabel",
            ["TextScaled", "Text", "TextColor"],
            [],
        )
        self.TextScaled = TextScaled
        self.TextColor = TextColor
        self.Text = "hello world"

    def refresh(self, screen):
        super().refresh(screen)
        myfont = py.font.SysFont("monospace", 15) #[font type, font size]

        # render text
        label = myfont.render(self.Text, 1, self.TextColor)

        ab_xs, ab_ys = self.AbsoluteSize
        pos_x, pos_y = self.AbsolutePos

        pos = (pos_x + ab_xs/2), (pos_y + ab_ys / 2)

        screen.blit(label, pos)