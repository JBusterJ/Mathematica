import pyglet
import random
from pyglet import shapes
import puremath as veryHighQualityMathThatIsDefinitelyOptimisedAndGivesYouTheMostAccurateResults

window = pyglet.window.Window(
    1000, 1000, "RMO (Runtime Mathematical Operator)", resizable=True)
batch = pyglet.graphics.Batch()

allShapes = [shapes.Rectangle(
    200, 200, 200, 200, color=(55, 55, 255), batch=batch)]
allLabels = []
prevCoord = []

data = ""


@window.event
def on_key_press(symbol, modifiers):
    # check if symbol is a modifier key
    # if (modifiers > 0):
    #     return
    # else:
    #     global data
    #     data = data[:-1]
    #     if symbol == pyglet.window.key.BACKSPACE:
    #         data = data[:-1]
    #         data += "_"
    #     else:
    #         data += chr(symbol) + "_"
    global allShapes
    global allLabels
    global batch
    global prevCoord
    if symbol == pyglet.window.key.C:
        allLabels = []
        allShapes = []
        prevCoord = []
        batch = pyglet.graphics.Batch()
        window.clear()
    elif symbol == pyglet.window.key.Z and len(allShapes) > 0:
        allShapes.pop()
        if len(prevCoord) > 0:
            prevCoord.pop()
        if len(allLabels) > 0:
            allLabels.pop()
        print(len(allLabels))

@window.event
def on_draw():
    window.clear()
    # allLabels[0] = pyglet.text.Label(str(data),
    #                         font_name='Times New Roman',
    #                         font_size=36,
    #                         x=window.width//2, y=window.height//2,
    #                         anchor_x='center', anchor_y='center')
    batch.draw()

# mouse click


@window.event
def on_mouse_press(x, y, button, modifiers):
    global allLabels
    global allShapes
    global prevCoord

    print(f"[{x}, {y}]\nOfType{button}")
    # colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    colour = (255, 255, 255)
    prevCoord.append((x, y))
    if len(prevCoord) > 1:
        # print(
            # f"prev: {prevCoord}, cur: ({x}, {y})\nlast coordinate: {prevCoord[-1]}")
        allShapes.append(shapes.Line(prevCoord[-2][0], prevCoord[-2][1], x,
                                    y, 1, color=(255, 225, 255), batch=batch))
    allShapes.append(shapes.Circle(x, y, 5, color=colour, batch=batch))
    allLabels.append(pyglet.text.Label(f"({str(x)},{str(y)})",
                                    font_name='Times New Roman',
                                    font_size=15,
                                    x=x, y=y-7.5,
                                    anchor_x='center', anchor_y='center',
                                    batch=batch))


img = image = pyglet.image.load('pi.jpg.jpg')
window.set_icon(img)

pyglet.app.run()
