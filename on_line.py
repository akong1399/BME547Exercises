def y_on_line(x1, y1, x2, y2, x):
    slope = (y2-y1) / (x2-x1)
    y = y1 + slope * (x - x1)
    return y
