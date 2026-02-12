import pygame as py
from .GUIBase import GUIBase


class Image(GUIBase):
    def __init__(
        self, Pos, Size, BackgroundColor, ImagePath, zIndex=1, UIAspectRatio=None
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            zIndex,
            UIAspectRatio,
            "ImageLabel",
            ["ImagePath", "Image"],
            [],
        )
        self.ImagePath = ImagePath
        self.Image = py.image.load(ImagePath).convert_alpha()

    def refresh(self, screen):
        super().refresh(screen)

        ab_xs, ab_ys = self.AbsoluteSize
        pos_x, pos_y = self.AbsolutePos

        pos = (pos_x + ab_xs / 2), (pos_y + ab_ys / 2)

        # Assets\MartianBackground.png
        # Resize the original image to a new width of 100 and height of 50
        resized_image = py.transform.scale(self.Image, (ab_xs, ab_ys))

        screen.blit(resized_image, self.AbsolutePos)
