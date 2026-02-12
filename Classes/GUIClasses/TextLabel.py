import pygame as py
from .GUIBase import GUIBase


class TextLabel(GUIBase):
    def __init__(
        self,
        Pos,
        Size,
        BackgroundColor,
        TextColor,
        TextFont="monospace",
        TextSize: int = 1,
        zIndex=None,
        UIAspectRatio=None,
        TextScaled: bool = True,
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            zIndex,
            UIAspectRatio,
            "TextLabel",
            ["TextScaled", "Text", "TextColor", "TextSize", "TextFont"],
            [],
        )
        self.TextScaled = TextScaled
        self.TextColor = TextColor
        self.TextSize = TextSize
        self.TextFont = TextFont
        self.Text = "hello world"

    def refresh(self, screen):
        super().refresh(screen)

        ab_xs, ab_ys = self.AbsoluteSize
        pos_x, pos_y = self.AbsolutePos

        if self.TextScaled:
            # Start large
            base_size = 100
            font = py.font.SysFont(self.TextFont, base_size)

            text_width, text_height = font.size(self.Text)

            # Calculate scale factors
            scale_x = ab_xs / text_width
            scale_y = ab_ys / text_height

            # Pick smallest so text fits inside box
            scale = min(scale_x, scale_y)

            new_size = int(base_size * scale)

            font = py.font.SysFont(self.TextFont, new_size)
        else:
            font = py.font.SysFont(self.TextFont, self.TextSize)

        # render text
        label = font.render(self.Text, 1, self.TextColor)

        fx, fy = font.size(self.Text)

        pos = (pos_x + ab_xs / 2 - fx / 2), (pos_y + ab_ys / 2 - fy / 2)

        screen.blit(label, pos)
