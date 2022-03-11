import pygame
import math as mathematics
from pygame import *

fileRead = open("inversekinematicruncounter.txt", "r+")

existingCounter = float(fileRead.read())
newCounter = existingCounter + 1

print(newCounter)

fileReadtoWrite = open("inversekinematicruncounter.txt", "w")
fileReadtoWrite.write(str(newCounter))

pygame.init()
pygame.display.set_caption(f'Inverse Kinematics [run {newCounter}]')


clock = pygame.time.Clock()
screen = pygame.display.set_mode([850, 500], pygame.RESIZABLE)


class arm:
    def __init__(self, position, fixed, lengthForArm):
        self.position = position
        self.fixed = fixed
        self.lengthForArm = lengthForArm

    def return_from_list(list):
        """ Converts a list of <arm> objects into a list with python tuples containing positions for each joint """
        positionsList = []
        lengthsList = []

        for i in range(len(list)):
            positionsList.append(list[i].position)
            lengthsList.append(list[i].lengthForArm)

        return [positionsList, lengthsList]

    def calculate_positions_for_point(positionList, positionForFinalPoint):
        """ Performs inverse kinematics calculations to find the joint positions given the position of the 'hand'"""
        finalPoint = positionList[-1]
        for i in range(len(positionList) - 1):
            pygame.draw.circle(screen, (255, 255, 255), (
                positionList[i].position[0], positionList[i].position[1]), positionList[i].lengthForArm, 1)
            try:
                if (i == len(positionList) - 2):
                    m = -((positionForFinalPoint[0]-positionList[i].position[0])/(positionForFinalPoint[1]-positionList[i].position[1]))
                    c = positionList[i].position[1]
                    # x = (positionForFinalPoint[1] - c)/m
                    # y = positionForFinalPoint[1]
                    h = positionList[i].position[0]
                    k = positionList[i].position[1]
                    r = positionList[i].lengthForArm 
                    # print(m, c, x, y, h, k, r)
                    # print((x**2) - (2*h*x) + (h**2) + (c**2) +((m**2) * (x**2)) -
                    #      (2*c*k) + (2*c*x*m) - (2*k*x*m) + (k**2) == (r**2))
                    print((h-(c*m)+(m*k)+mathematics.sqrt(abs(-((m**2)*(h**2))+(2*m*k*h)-(2*c*m*h)+(2*c*k)+((m**2)*(r**2))+(r**2)-(c**2)-(k**2))/1+(m**2))))
                    # print(f"{y}={m}*{x}+{c}")

                # if (mathematics.sqrt((abs(positionList[i].position[0]-positionList[i+1].position[0]))**2+(abs(positionList[i].position[1]-positionList[i+1].position[1]))**2) > positionList[i].lengthForArm):
                #     # finalPoint.position = (abs(positionList[-1].position[0] - finalPoint.position[0]), abs(positionList[-1].position[1] - finalPoint.position[1]))
                #     finalPoint.position = positionForFinalPoint
                # else:
                #     finalPoint.position = positionForFinalPoint

                finalPoint.position = positionForFinalPoint

                # print (f"finalPoint: {finalPoint.position}\nxDifferences: {abs(positionList[i-1].position[0] - finalPoint.position[0])}\nyDifferences: {abs(positionList[i-1].position[1] - finalPoint.position[1])}\ndistance: {mathematics.sqrt((abs(positionList[i-1].position[0] - finalPoint.position[0]))**2+(abs(positionList[i-1].position[1] - finalPoint.position[1]))**2)}")
                pygame.draw.line(
                    screen, (255, 255, 255), positionList[i+1].position, positionList[i].position)
                # print (f"angle calculations {mathematics.acos((abs(positionList[i-1].position[0] - finalPoint.position[0]))/(abs(positionList[i-1].position[1] - finalPoint.position[1])))}")
            except Exception as e:
                print(e)
        for i in range(len(positionList)):
            pygame.draw.circle(screen, (252, 186, 3),
                               positionList[i].position, 5)


def createArms(amount, length, position):
    """ Create a joint for running the inverse kinematic(s) algorith\nAccepts the amount of arms, the length of each arm, and the position of the fixed arm. """
    previousArmPosition = position
    arms = []

    for i in range(0, amount):
        if i == 0:
            arms.append(arm(position, True, length))
        else:
            arms.append(arm(previousArmPosition, False, length))

        previousArmPosition = (
            previousArmPosition[0] + length, previousArmPosition[1])

    return arms


arms = createArms(5, 100, (250, 250))

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    screen.fill((47, 54, 74))

    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont("times new roman", 20)
    text = font.render(str(mouse_pos), True, (255, 255, 255))
    screen.blit(
        text, (mouse_pos[0] - (text.get_width()/2), mouse_pos[1] - (3*text.get_height()/2)))

    arm.calculate_positions_for_point(arms, (mouse_pos[0], mouse_pos[1]))

    pygame.display.flip()


pygame.quit()
