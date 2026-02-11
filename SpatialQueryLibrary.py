

def PointInsideRectange(RecSize, RecPos, MousePos):
    #this library assumes that the rectangle is centered, also that the screen start in the top right corner

    x_pos, y_pos = RecPos
    x_size, y_size = RecSize

    xMP, yMP = MousePos

    #Left Bound (LB); Right Bound (RB)
    xlb, xrb = x_pos - x_size/2, x_pos + x_size/2
    #Top Bound (TB); Bottem Bound (BB)
    ytb, ybb = y_pos - y_size/2, y_pos + y_size/2

    if xMP < xlb:
        return False
    elif xMP > xrb:
        return False
    elif yMP < ytb:
        return False
    elif yMP > ybb:
        return False
    
    return True