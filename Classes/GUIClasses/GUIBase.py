from Classes.SuperClass import SuperClass
import pygame as py

guiAssetList = []


def clamp(value, minVal, maxVal):
    return max(minVal, min(value, maxVal))

class GUIBase(SuperClass):
    def __init__(
        self,
        Pos,
        Size,
        Color,
        BackgroundTransparency: int = 1,
        zIndex: int = 1,
        UIAspectRatio: float = None,
        ClassName: str = "GuiBase",
        ValidProperties=[],
        SignalProperties=[],
    ):  # UI Aspect Ratio the main axis is x, also size being limited on the x-axis
        ValidProperties = ValidProperties + [
            "Pos",
            "Size",
            "BackgroundColor",
            "BackgroundTransparency",
            "zIndex",
            "UIAspectRatio",
            "AbsolutePos",
            "AbsoluteSize",
            "Visible",
            "BorderThickness",
            "BorderColor"
        ]
        SignalProperties = SignalProperties + [
            "Pos",
            "Size",
            "zIndex",
            "BackgroundColor",
        ]
        super().__init__(ClassName, ValidProperties, SignalProperties)
        self.Pos = Pos
        self.Size = Size
        self.AbsolutePos = (0, 0)
        self.AbsoluteSize = (0, 0)
        self.BackgroundColor = Color
        self.BackgroundTransparency = clamp(BackgroundTransparency, 0, 1)
        self.zIndex = zIndex
        self.Visible = True
        self.UIAspectRatio = UIAspectRatio
        #add ts please
        self.BorderThickness = 0
        self.BorderColor = (255,0,255)
        guiAssetList.append(self)

    def refresh(self, screen):
        if not self.Visible:
            return True
        ScreenWidth, ScreenHeight = screen.get_size()

        xs, ys = self.Size

        xs, ys = xs * ScreenWidth, ys * ScreenHeight

        xp, yp = self.Pos

        # Check for aspect ratio
        if self.UIAspectRatio:
            ys = xs * self.UIAspectRatio

        xp, yp = xp * ScreenWidth - xs / 2, yp * ScreenHeight - ys / 2

        self.AbsolutePos = (xp, yp)
        self.AbsoluteSize = (xs, ys)

        if self.BackgroundTransparency == 1:
            # No need to draw rectangle as the background transpareny is 1
            return

        rectDetails = py.Rect(xp, yp, xs, ys)

        py.draw.rect(screen, self.BackgroundColor, rectDetails)
        if self.BorderThickness > 0:
            py.draw.rect(screen, self.BorderColor, rectDetails, self.BorderThickness)


def GetGuiAssets():
    global guiAssetList

    sortedAssetList = []
    sortedAssetDic = {}
    for guiItem in guiAssetList:
        if guiItem.zIndex not in sortedAssetDic:
            sortedAssetDic[guiItem.zIndex] = []
        sortedAssetDic[guiItem.zIndex].append(guiItem)

    sortedAssetDic = dict(sorted(sortedAssetDic.items()))
    for row in sortedAssetDic.values():
        # print(row)
        for item in row:
            sortedAssetList.append(item)

    return sortedAssetList
