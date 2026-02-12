from Classes.SuperClass import SuperClass
import pygame as py

guiAssetList = []


class GUIBase(SuperClass):
    def __init__(
        self,
        Pos,
        Size,
        Color,
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
            "zIndex",
            "UIAspectRatio",
            "AbsolutePos",
            "AbsoluteSize",
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
        self.zIndex = zIndex
        self.UIAspectRatio = UIAspectRatio
        guiAssetList.append(self)

    def refresh(self, screen):
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

        rectDetails = py.Rect(xp, yp, xs, ys)

        py.draw.rect(screen, self.BackgroundColor, rectDetails, 0)


def GetGuiAssets():
    global guiAssetList

    sortedAssetList = []
    sortedAssetDic = {}
    for guiItem in guiAssetList:
        if guiItem.zIndex not in sortedAssetDic:
            sortedAssetDic[guiItem.zIndex] = []
        sortedAssetDic[guiItem.zIndex].append(guiItem)
    print(sortedAssetDic.items())
    sortedAssetDic = dict(sorted(sortedAssetDic.items()))
    for row in sortedAssetDic.values():
        #print(row)
        for item in row:
            sortedAssetList.append(item)

    return sortedAssetList
