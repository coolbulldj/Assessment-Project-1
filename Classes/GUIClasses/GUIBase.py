import pygame as py


class GUIBase():

    def __init__(self, Pos, Size, Color, UIAspectRatio:float=None): #UI Aspect Ratio the main axis is x
        self.Pos = Pos
        self.Size = Size
        self.BackgroundColor = Color
        self.UIAspectRatio = UIAspectRatio

    def refresh(self, screen):
        
        ScreenWidth, ScreenHeight = screen.get_size()

        x, y = self.Pos
        xs, ys = self.Size
        #rel_x, rel_y = x, y
        rel_x, rel_y = (x - xs/2, y - ys/2)
        #Apply real absolute position & size
        rel_x, rel_y = rel_x * ScreenWidth, rel_y * ScreenHeight
        xs, ys = xs * ScreenWidth, ys * ScreenHeight

        rectDetails = py.Rect(rel_x, rel_y, xs, ys)

        py.draw.rect(screen, self.BackgroundColor, rectDetails, 0)
