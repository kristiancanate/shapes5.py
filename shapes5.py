from graphics import *

sWin = GraphWin("5 Shapes", 300, 300)
sWin.setCoords(0, 0, 300, 300)

#First Object (Red Pentagon)
rPen = Polygon(Point(25, 210), Point(10, 260), Point(50, 290),
               Point(90, 260), Point(75, 210))
rPen.setFill(color_rgb(255, 0, 0))
rPen.draw(sWin)

#Second Object (Orange Hexagon)
oHex = Polygon(Point(180, 240), Point(205, 290), Point(265, 290),
               Point(290, 240), Point(265, 190), Point(205, 190))
oHex.setFill(color_rgb(255, 128, 0))
oHex.draw(sWin)

#Third Object (Yellow Septagon)
ySep = Polygon(Point(190, 10), Point(150, 60), Point(165, 120), 
               Point(220, 150), Point(275, 120), Point(290, 60),
               Point(250, 10))
ySep.setFill(color_rgb(255, 255, 0))
ySep.draw(sWin)

#Fourth Object (Green Octagon)
gOct = Polygon(Point(30, 10), Point(10, 30), Point(10, 50), 
               Point(30, 70), Point(50, 70), Point(70, 50),
               Point(70, 30), Point(50, 10))
gOct.setFill(color_rgb(51, 204, 51))
gOct.draw(sWin)

sWin.getMouse()
sWin.close()
