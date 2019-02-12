from graphics import *

sWin = GraphWin("5 Shapes", 300, 300)
sWin.setCoords(0, 0, 300, 300)

#First Object (Pentagon)
rPen = Polygon(Point(25, 210), Point(10, 260), Point(50, 290), Point(90, 260), Point(75, 210))
rPen.setFill(color_rgb(230, 30, 30))
rPen.draw(sWin)

sWin.getMouse()
sWin.close()
