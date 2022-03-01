import math
import puremath as extras
import random
import os
import os.path
import cairo

imagesize = (10, 10)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)

cr = cairo.Context(surface)

cr.set_source_rgba(0.0, 0.0, 0.0)
cr.rectangle(0, 0, *imagesize)
cr.fill()

cr.set_source_rgb(1, 1, 1)

def generateCells(startX, startY, cells, densityModifier, dotSize):
    cellArrays = []
    ray = []
    
    if (dotSize == 0):
        dotSize = 1
    
    curPositions = [startX, startY]
    # for x in range(cells):
    #     curPositions[0] += (1 * densityModifier)
    #     curPositions[1] += (1 * densityModifier)
    #     cr.move_to(curPositions[0], curPositions[1])
    #     cr.fill()
    #     cr.set_source_rgba(1.0, 1.0, 1.0)
    #     cr.arc(curPositions[0], curPositions[1], dotSize, 0, 2 * math.pi)
    for trueX in range(cells):
        cr.move_to(curPositions[0], 0)
        cr.line_to(curPositions[0], cells)
        curPositions[0] += (2 * densityModifier)
    for trueY in range(cells):
        cr.move_to(0, curPositions[1])
        cr.line_to(cells, curPositions[1])
        curPositions[1] += (2 * densityModifier)
    for hypotenuseTriangularCalculationsY in range(cells):
        for hypotenuseTriangularCalculationsX in range(cells):
            if (len(ray) < cells):
                ray.append(0)
            else:
                cellArrays.append(ray)
                ray = []

    print (cellArrays)

    return curPositions

def cellModifier(data, assumePreviouslyGenerated):
    if (assumePreviouslyGenerated):
        for x in range(data):
            for y in range(len(data[i])):
                return data
        return data
    else:
        return generateCells(0, 0, data, 1, 0)
    pass

print(generateCells(0, 0, 10, 5, 3))

cr.move_to(0, 0)
# cr.line_to(256, 256)

cr.stroke()

fn = random.randrange(1, 50)

surface.write_to_png(
    f"output/barycentrics/_{len([name for name in os.listdir('output/barycentrics')]) + 1}-output.png")
# surface.write_to_png(
#     f"output/barycentrics/{random.randint(0, 100)}-output.png")