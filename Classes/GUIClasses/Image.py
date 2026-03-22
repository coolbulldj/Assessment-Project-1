import pygame as py
from .GUIBase import GUIBase

CachedImages = {}

def getImage(ImagePath:str):
    if ImagePath not in CachedImages:
        CachedImages[ImagePath] = py.image.load(ImagePath).convert_alpha()
    return CachedImages[ImagePath]

class Image(GUIBase):
    def __init__(
        self,
        Pos,
        Size,
        BackgroundColor,
        BackgroundTranspareny,
        ImagePath,
        zIndex=1,
        UIAspectRatio=None,
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            BackgroundTranspareny,
            zIndex,
            UIAspectRatio,
            "ImageLabel",
            ["ImagePath", "Image"],
            ["ImagePath"],
        )
        self.ImagePath = ImagePath
        self.Image = getImage(ImagePath)

        def updateImage(newImagePath):
            #print("updating image")
            self.Image = getImage(newImagePath)

        self.GetPropertyChangedSignal("ImagePath").Connect(updateImage)

    def refresh(self, screen):
        if super().refresh(screen): #this means the super is invisible
            #print(self.Visible)
            return

        ab_xs, ab_ys = self.AbsoluteSize


        # Assets\MartianBackground.png
        # Resize the original image to a new width of 100 and height of 50
        resized_image = py.transform.scale(self.Image, (ab_xs, ab_ys))

        screen.blit(resized_image, self.AbsolutePos)
