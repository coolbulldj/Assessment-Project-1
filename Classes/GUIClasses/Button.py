from .GUIBase import GUIBase
from ..EventClass import Event
from SpatialQueryLibrary import PointInsideRectange

buttonList = {
    "MouseUp" : [],
    "MouseDown" : []
}

class Button(GUIBase):
    def __init__(
        self, Pos, Size, BackgroundColor, zIndex=1, UIAspectRatio=None
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            zIndex,
            UIAspectRatio,
            "GuiButton",
            ["OnMouseDown", "OnMouseUp", "MouseClickOff"],
            [],
        )
        self.MouseDown = Event()
        self.MouseUp = Event()
        self.MouseClickOff = Event()
        buttonList["MouseUp"].append(self.MouseUp)
        buttonList["MouseDown"].append(self.MouseDown)


    def FireMouseDown(self, screen, MousePos):
        xs, ys = screen.get_size()
        xm, ym = MousePos
        scaledMousePos = (xm / xs, ym / ys)
        if PointInsideRectange(self.Size, self.Pos, scaledMousePos):
            self.MouseDown._FireEvent()
        else:
            self.MouseClickOff._FireEvent()

    def FireMouseUp(self, screen, MousePos):
        xs, ys = screen.get_size()
        xm, ym = MousePos
        scaledMousePos = (xm / xs, ym / ys)
        if PointInsideRectange(self.Size, self.Pos, scaledMousePos):
            self.MouseUp._FireEvent()
        else:
            self.MouseClickOff._FireEvent()

    
def getButtonList():
    return buttonList