import os
import cairo
import random
import pyglet
from pyglet.gl import *
import math


# set up pyglet
window = pyglet.window.Window(width=1000, height=500, resizable=True)
batch = pyglet.graphics.Batch()

imagesize = (512, 512)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)

cr = cairo.Context(surface)

# paint background
cr.set_source_rgba(0.0, 0.0, 0.0, 0.0)  # transparent black
cr.rectangle(0, 0, 512, 512)
cr.fill()

cr.set_source_rgb(1, 1, 1)

x = math.sin(60)/512

print(512 / x)

cr.move_to(0, 512)
cr.line_to(256, 512 / x)

cr.stroke()

fn = random.randrange(1, 50)


surface.write_to_png(f"output/{fn}.png")

image = pyglet.image.load(f'output/{fn}.png')


# load screen
@window.event
def on_draw():
    print(window.get_size());
    window.clear()
    image.blit(0, 0)



# finish pyglet
pyglet.app.run()
