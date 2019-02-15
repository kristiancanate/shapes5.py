from graphics import *

sWin = GraphWin("5 Shapes", 300, 300)
sWin.setCoords(0, 0, 300, 300)

#First Object (Pentagon)
rPen = Polygon(Point(25, 210), Point(10, 260), Point(50, 290),
               Point(90, 260), Point(75, 210))
rPen.setFill(color_rgb(255, 0, 0))
rPen.draw(sWin)

#Second Object (Hexagon)
oHex = Polygon(Point(180, 240), Point(205, 290), Point(265, 290),
               Point(290, 240), Point(265, 190), Point(205, 190))
oHex.setFill(color_rgb(255, 128, 0))
oHex.draw(sWin)

sWin.getMouse()
sWin.close()
