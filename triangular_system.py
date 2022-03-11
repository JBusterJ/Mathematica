import math
import os
import random
import sys
import time
import cairo
import re
import numpy
from sympy import *

# intialize cairo


def init_cairo(width, height):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    return ctx

# draw a grid


def draw_grid(ctx, width, height, cell_size):
    ctx.set_line_width(0.5)
    ctx.set_source_rgb(0.2, 0.64, 0.74)
    for i in range(0, width, cell_size):
        ctx.move_to(i, 0)
        ctx.line_to(i, height)
    for i in range(0, height, cell_size):
        ctx.move_to(0, i)
        ctx.line_to(width, i)
    ctx.stroke()

# draw the triangular system


def draw_system(ctx, width, height, cell_size):
    # for i in range(0, (width * 2), cell_size):
    #     ctx.move_to(0, i)
    #     ctx.line_to(i, 0)
    # for x in range(0, (width * 2), cell_size):
    #     ctx.move_to(0, x)
    #     ctx.line_to(width, x + width)
    #     ctx.move_to(x, x)
    #     ctx.line_to(width, width - x)

    xCoordinates = []
    yCoordinates = []

    totalCoordinates = []

    ctx.set_line_width(0.5)
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            if len(yCoordinates) % cell_size == 0:
                totalCoordinates.append(yCoordinates)
                yCoordinates = []
            ctx.move_to(x, y)
            ctx.line_to(x + cell_size, y + cell_size)
            ctx.move_to(x, y + cell_size)
            ctx.line_to(x + cell_size, y)

    ctx.stroke()
    print(totalCoordinates)

# save the image


def save_image(ctx, filename):
    surface = ctx.get_target()
    surface.write_to_png(filename)


def draw_function(ctx, width, height, cell_size, function):
    # replace all letters with a random number
    pastPosition = (-width / 2, height / 2)
    func = function.replace("x", "i")

    func = func.replace("^", "**")

    ctx.set_source_rgb(0, 0, 0)

    if ("()" in func):
        transposedString = transposeInString(func, "y")
        for i in range(int(-width / 2), int(width / 2), cell_size):
            print(transposedString)
            func = func.replace("y", transposedString)
            pass
    else:
        for i in range(int(-width / 2), int(width / 2), cell_size):
            if i < 0:
                ctx.move_to(abs(width / 2 + i), height / 2 + eval(func))
                ctx.line_to(abs(width / 2 + pastPosition[0]), pastPosition[1])
                pastPosition = (i, height / 2 + eval(func))
            else:
                ctx.move_to((width / 2) + i, height / 2 + eval(func))
                ctx.line_to((width / 2) + pastPosition[0], pastPosition[1])
                pastPosition = (i, height / 2 + eval(func))
    ctx.stroke()


def transposeInString(string, subject):
    string = string.replace(" ", "")
    eq = sympify(string)
    newEQ = solve(eq, subject)
    print(newEQ)
    return newEQ


# string = "a^2+b^2-c^2"
# eq = sympify(string)
# newEQ = solve(eq, "a")
# print(string, eq, newEQ)

lengthTuple = (2048, 2048)

ctx = init_cairo(lengthTuple[0], lengthTuple[1])

draw_grid(ctx, lengthTuple[0], lengthTuple[1], 50)
# draw_function(ctx, lengthTuple[0], lengthTuple[1],
#             10, f"math.sin(((i))*1/50)*100")
# draw_function(ctx, lengthTuple[0], lengthTuple[1], 1, "x^2+y^2-3^2 ()")

# draw_function(ctx, lengthTuple[0], lengthTuple[1],
#             1, f"math.cos(i)*i")
# draw_random_curve(ctx, lengthTuple[0], lengthTuple[1], 5, 5)
# draw_system(ctx, lengthTuple[0], lengthTuple[1], 50)
# draw_function(ctx, lengthTuple[0], lengthTuple[1], 1, "(-math.sqrt(abs(numpy.arcsin(math.cos(x))-x**2)))")
# draw_function(ctx, lengthTuple[0], lengthTuple[1], 1, "math.sqrt(abs(math.sin(math.cos(x*10)+x**2)))*50")
draw_function(ctx, lengthTuple[0], lengthTuple[1], 1, "(x-2.5)**2+8")

# get number of files in output folder
files = os.listdir('output/barycentrics')
save_image(
    ctx, f"output/barycentrics/__#{len(files)}-number-files#__.png")
