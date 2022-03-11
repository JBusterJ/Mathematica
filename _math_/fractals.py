# WHY DID I START MAKING THIS?????????????? FRACTALS SOUND TOO COMPLICATED CAUSE I NEED TO:
# IMPORT SOME GRAPHICS LIBRARY
# COMPLEX MATH FOR COMPLEX FRACTALS
# I DIDN'T THINK THIS PROJECT THROUGH DID I!??!??
# I MEAN THE MANDELBROT SET IS SIMPLE AND I BET THERE ARE MANY OTHERS THAT ARE AS SIMPLE AS THAT BUT STILL VERY POPULAR AND BEAUTIFUL
# BUT EH
# Import statement for library. Can be imported in multiple ways but this way is the most effective in my opinion. You can also only load specific classes / definitions inside the main file but I am not exactly sure what operations I even need to make fractals show up on the screen.
# from graphics import *  # gfx lib
import turtle as graphics
from puremath import Math
import math
core = Math()
import os

# starting of by testing the Koch Snowflake - F → F+F--F+F - I will initially avoid the use of any operations built by yours truly because I am sure there are bugs and glitches that will impact perfomance of the outcome.
# F = draw forward, - = turn right 60 deg, + = turn left 60 deg
# Axiom = F--F--F
# Looks simple.... heh... right?

# draw forward, turn 60 degrees left, move forward, turn 120 degrees right, move forward, turn 60 degrees left, move forward


# def KochFractal(length, lod):
#     # length is self explanatory
#     # lod = level of detail, or, in other words, the magnification of the fractal
#     F = length
#     currentPos = Point(0, 0)

#     win = GraphWin('Koch Fractal', 1000, 500)
#     win.setCoords(0, 0, 1000, 500)

#     # generate a list of vertices of triangle that will have a side length of length
#     def generateTriangle(sideLength, origin, array):
#         # generate a list of vertices of triangle that will have a side length of length
#         # the vertices are in the form of a list of tuples
#         # the vertices are in the form of a list of tuples
#         vertices = [Point(origin[0] + array[0], origin[1] + array[1]), Point(
#             origin[0] + sideLength, origin[1]), Point(origin[0] + sideLength/2, origin[1] + sideLength * math.sqrt(3)/2)]
#         return vertices

#     # Use Polygon object to draw the triangle
#     triangle = Polygon(generateTriangle(F, [500 * 25/100, 500 * 25/100], [0, 0]))
#     triangle.setFill('gray')
#     triangle.draw(win)

#     print(f'{triangle.getPoints()}')

#     points = triangle.getPoints()

#     currentPos = Point(500 * 25/100, 500 * 25/100)

#     for i in range(2, lod):
#         print(F / i)

#         triangleHeight = math.sqrt((3 * (F / i) * (F / i)) / 4)

#         lowerQuartile = (F / i) / 2 * 0.5
#         upperQuartile = (F / i) / 2 * 1.5


#         b = (upperQuartile * math.tan(30))

#         print(f"currentPos: {currentPos}, \nb: {b}, \nupperQuartile: {upperQuartile}")

#         tangle = generateTriangle(
#             F / i, [(currentPos.getX() + F / i), points[1].getY() + upperQuartile], [0,  points[1].getY() + upperQuartile])
#         t2 = Polygon(tangle)
#         currentPos = Point((currentPos.getX() + F / i), currentPos.getY() + upperQuartile)
#         t2.setFill('orange')
#         t2.draw(win)

#     win.getMouse()
#     win.close()

cmd = "wmic path Win32_VideoController get CurrentVerticalResolution,CurrentHorizontalResolution"
size_tuple = tuple(map(int,os.popen(cmd).read().split()[-2::]))

# F = draw forward, - = turn right 60 deg, + = turn left 60 deg
# F → F+F--F+F

def KochFractal(length, ithink):
    graphics.setup(size_tuple[0] / 2, size_tuple[1] / 2, 0, 0)
    graphics.hideturtle()
    graphics.speed(0)
    graphics.penup()
    graphics.goto(-length / 2, -length / 2)
    graphics.pendown()
    graphics.setheading(0)

    graphics.forward(length)
    graphics.left(120)
    graphics.forward(length)
    graphics.left(120)
    graphics.forward(length)
    graphics.left(120)

    graphics.setheading(0)
    graphics.penup()

    prevUpperQuartile = (length / 2) * 1.5
    prevLowerQuartile = (length / 2) * 0.5

    for i in range(2, ithink):
        lowerQuartile = ((length / i) / 2) * 0.5
        upperQuartile = ((length / i) / 2) * 1.5

        b = (prevUpperQuartile * math.tan(30))

        graphics.goto((-length / 2 + length) - (prevUpperQuartile / 2 + length / (i * 20)), -length / 2 + prevUpperQuartile)
        graphics.pendown()

        graphics.forward((length / i))
        graphics.right(120)
        graphics.forward((length / i))
        graphics.penup()

        graphics.setheading(0)

        prevUpperQuartile = upperQuartile
        prevLowerQuartile = lowerQuartile

    graphics.Screen().exitonclick()

KochFractal(100, 100)
