import pygame
import math as mathematics
import random
import pygame
from pygame import *

fileRead = open("inversekinematicruncounter.txt", "r+")

existingCounter = fileRead.read()
newCounter = float(existingCounter) + 1

fileReadtoWrite = open("inversekinematicruncounter.txt", "w")
fileReadtoWrite.write(str(newCounter))

pygame.init()
pygame.display.set_caption(f'Inverse Kinematics (rewrite) [run {newCounter}]')


clock = pygame.time.Clock()
screen = pygame.display.set_mode([850, 500], pygame.RESIZABLE)


def coord(x, y):
    """Converts cartesian coordinates to pygame coordinates, (0, 0) being the center of the screen"""
    return (850/2 + x, 500/2 - y)


def pyCoord(x, y):
    """Converts pygame coordinates to cartesian coordinates, (0, 0) being the top left of the screen"""
    return (x - 850 / 2, y - 500 / 2)


def tupleAddition(tuple1, tuple2):
    """Utility function for adding tuples"""
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def tripleTupleAddition(tuple1, tuple2):
    """Utility function for adding Vectors with 3 dimensions"""
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1], tuple1[2] + tuple2[2])


def drawDashedLine(x1, y1, x2, y2, dashLength=10):
    isDashed = False
    x = x1
    y = y1
    deltaX = x2 - x1
    deltaY = y2 - y1
    distance = mathematics.sqrt(deltaX ** 2 + deltaY ** 2)
    noOfDashes = distance / dashLength
    angle = mathematics.atan2(deltaY, deltaX)
    while x <= x2:
        if isDashed:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x + dashLength *
                             mathematics.cos(angle), y + dashLength * mathematics.sin(angle)))
        else:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x + dashLength *
                             mathematics.cos(angle), y + dashLength * mathematics.sin(angle)))
        isDashed = not isDashed
        x += dashLength * mathematics.cos(angle)
        y += dashLength * mathematics.sin(angle)


class arm:
    def __init__(self, position, length, isFixed, color, size):
        self.position = position
        self.length = length
        self.isFixed = isFixed
        self.color = color
        self.size = size

    def generate(amount, intialArm):
        list = []
        lastArm = intialArm
        for i in range(amount):
            color = (245, 93, 66)
            size = 3
            if (lastArm.isFixed):
                color = (219, 147, 31)
                size = 5
            newArm = arm(tupleAddition(
                lastArm.position, (lastArm.length, 0)), lastArm.length, False, color, size)

            lastArm = newArm
            list.append(lastArm)
        return list

    def drawLines(list, limitPoint, toDrawNormally):
        for i in range(len(list)):
            try:
                if (i == len(list) - 1):
                    pygame.draw.circle(screen, (66, 245, 96),
                                       list[i].position, list[i].length, 1)
                else:
                    pygame.draw.circle(screen, (255, 255, 255),
                                       list[i].position, list[i].length, 1)
            except:
                pass
        for i in range(len(list) - 1):
            try:
                pygame.draw.circle(screen, (255, 255, 255),
                                   list[i + 1].position, 3, 3)
                if (i == len(list) - 2):
                    if (toDrawNormally):
                        pygame.draw.line(screen, (255, 134, 82),
                                         list[i].position, list[i+1].position, 5)
                    else:
                        pygame.draw.line(screen, (255, 134, 82),
                                         list[i].position, coord(limitPoint[0], limitPoint[1]), 3)
                        pygame.draw.line(screen, (255, 0, 0), coord(
                            limitPoint[0], limitPoint[1]), list[i + 1].position, 1)
                else:
                    pygame.draw.line(screen, (255, 255, 255),
                                     list[i].position, list[i+1].position, 1)
                pygame.draw.circle(
                    screen, list[i].color, list[i].position,  list[i].size, list[i].size)
            except Exception as e:
                print(e)

    def alterPosition(self, position, **args):
        self.position = position
        if (len(args) > 0):
            self.length = args["length"]
            self.isFixed = args["isFixed"]
            self.color = args["color"]
            self.size = args["size"]

    def kinematics(list):
        for i in range(len(list))[::-1]:
            if (i == len(list) - 1):
                r = list[i-1].length
                (h, k) = pyCoord(list[i].position[0], list[i].position[1])
                y = -pyCoord(0, list[i-1].position[1])[1]
                if (list[i].position[0] < list[i-1].position[0]):
                    x = -mathematics.sqrt((r**2)-(y**2)+(2*k*(y**2))-(k**2))+h
                else:
                    x = mathematics.sqrt((r**2)-(y**2)+(2*k*(y**2))-(k**2))+h

                # print((x, y))

                pygame.draw.circle(screen, (255, 255, 255), coord(x, y), 3, 3)

running = True
mousePosition = (100, 100)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePosition = pygame.mouse.get_pos()

    screen.fill((47, 54, 74))
    for x in range(-500, 500, 10):
        pygame.draw.line(screen, (105, 105, 105),
                         coord(x, -500), coord(x, 500), 1)
    for y in range(-850, 850, 10):
        pygame.draw.line(screen, (105, 105, 105),
                         coord(-850, y), coord(850, y), 1)
    pygame.draw.line(screen, (255, 255, 255), coord(0, -500), coord(0, 500), 1)
    pygame.draw.line(screen, (255, 255, 255), coord(-850, 0), coord(850, 0), 1)

    # pygame.draw.circle(screen, (255, 255, 255), coord(10, 10), 2, 2)
    starterArm = arm(coord(-100, 0), 100, True, (255, 255, 255), 3)
    armList = arm.generate(3, starterArm)

    arm.alterPosition(armList[-1], mousePosition)

    lengthFromOrigin = mathematics.sqrt(abs(
        armList[-1].position[0]-armList[-2].position[0])**2 + abs(armList[-1].position[1]-armList[-2].position[1])**2)

    xIntersection = 0
    yIntersection = 0

    if (lengthFromOrigin > armList[-2].length):
        try:
            m = -(armList[-1].position[1]-armList[-2].position[1]) / - \
                (armList[-2].position[0]-armList[-1].position[0])

            c = pyCoord(0, armList[-2].position[1])[1] - \
                (m * pyCoord(armList[-2].position[0], 0)[0])

            h = pyCoord(armList[-2].position[0], 0)[0]

            k = pyCoord(0, armList[-2].position[1])[1]

            r = armList[-2].length

            if (armList[-1].position[0] < armList[-2].position[0] and armList[-1].position[1] < armList[-2].position[1]):
                xIntersection = (h-(c*m)+(m*k)-(mathematics.sqrt(-(m**2*h**2) +
                                                                 (2*m*k*h)-(2*c*m*h)+(2*c*k)+(m**2*r**2)+r**2-c**2-k**2))) / (m**2 + 1)
                yIntersection = (c+(h*m)+(m**2*k)-m*mathematics.sqrt(-(c**2)+(2*k*c) -
                                                                     (2*h*m*c)+(2*h*m*k)+(m**2*r**2)+r**2-(h**2*m**2) - k**2)) / (m**2 + 1)
            elif (armList[-1].position[0] > armList[-2].position[0] and armList[-1].position[1] > armList[-2].position[1]):
                xIntersection = (h-(c*m)+(m*k)+(mathematics.sqrt(-(m**2*h**2) +
                                                                 (2*m*k*h)-(2*c*m*h)+(2*c*k)+(m**2*r**2)+r**2-c**2-k**2))) / (m**2 + 1)
                yIntersection = (c+(h*m)+(m**2*k)+m*mathematics.sqrt(-(c**2)+(2*k*c) -
                                                                     (2*h*m*c)+(2*h*m*k)+(m**2*r**2)+r**2-(h**2*m**2) - k**2)) / (m**2 + 1)
            elif (armList[-1].position[0] > armList[-2].position[0] and armList[-1].position[1] < armList[-2].position[1]):
                xIntersection = (h-(c*m)+(m*k)+(mathematics.sqrt(-(m**2*h**2) +
                                                                 (2*m*k*h)-(2*c*m*h)+(2*c*k)+(m**2*r**2)+r**2-c**2-k**2))) / (m**2 + 1)
                yIntersection = (c+(h*m)+(m**2*k)+m*mathematics.sqrt(-(c**2)+(2*k*c) -
                                                                     (2*h*m*c)+(2*h*m*k)+(m**2*r**2)+r**2-(h**2*m**2) - k**2)) / (m**2 + 1)
            else:
                xIntersection = (h-(c*m)+(m*k)-(mathematics.sqrt(-(m**2*h**2) +
                                                                 (2*m*k*h)-(2*c*m*h)+(2*c*k)+(m**2*r**2)+r**2-c**2-k**2))) / (m**2 + 1)
                yIntersection = (c+(h*m)+(m**2*k)-m*mathematics.sqrt(-(c**2)+(2*k*c) -
                                                                     (2*h*m*c)+(2*h*m*k)+(m**2*r**2)+r**2-(h**2*m**2) - k**2)) / (m**2 + 1)

            pygame.draw.circle(screen, (255, 255, 255), coord(
                xIntersection, yIntersection), 5, 5)
            arm.drawLines(armList, (xIntersection, yIntersection), False)
        except:
            # undefined output means that the arm does not intersect with the
            xIntersection = "undefined"
            # same reason as above. either one could be undefined but we do not want to waste time differentiating between them
            yIntersection = "undefined"
            pass
    else:
        arm.kinematics(armList)
        arm.drawLines(armList, mousePosition, True)

    pygame.display.flip()
