import pyglet
from pyglet.gl import *
from pyglet.window import mouse
from pyglet import font
import settings
import time
import gamescene


class MenuScene:
    def __init__(self):
        self.goto = MenuScene
        pyglet.gl.glClearColor(0.1, 0.1, 0.1, 1)
        pyglet.font.add_file("hexagon_cup.ttf")
        pyglet.font.load('HEXAGON cup font')
        pyglet.font.add_file("CaviarDreams.ttf")
        pyglet.font.load('Caviar Dreams')
        self.header = pyglet.text.Label(
            'PyBattle',
            font_name='HEXAGON cup font',
            font_size=70,
            x=settings.width/2,
            y=settings.height-130,
            anchor_x='center',
            color=(35, 255, 204, 255))
        self.start_button = pyglet.text.Label(
            '⬡ START',
            font_name='Caviar Dreams',
            font_size=24,
            x=settings.width/2,
            y=settings.height-400,
            anchor_x='center',
            color=(35, 255, 204, 255)
        )
        self.settings_button = pyglet.text.Label(
            '⬡ SETTINGS',
            font_name='Caviar Dreams',
            font_size=24,
            x=settings.width/2,
            y=settings.height-450,
            anchor_x='center',
            color=(35, 255, 204, 255)
        )
        self.exit_button = pyglet.text.Label(
            '⬡ EXIT',
            font_name='Caviar Dreams',
            font_size=24,
            x=settings.width/2,
            y=settings.height-500,
            anchor_x='center',
            color=(35, 255, 204, 255)
        )

    def on_mouse_press(self):
        self.goto = gamescene.GameScene

    def on_draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', (521, 229,
                                      521, 428,
                                      846, 428,
                                      846, 229)),
                             ('c4B', (35, 255, 204, 255,
                                      35, 255, 204, 255,
                                      35, 255, 204, 255,
                                      35, 255, 204, 255)))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', (516, 224,
                                      516, 433,
                                      851, 433,
                                      851, 224)),
                             ('c4B', (35, 255, 204, 255,
                                      35, 255, 204, 255,
                                      35, 255, 204, 255,
                                      35, 255, 204, 255)))
        self.header.draw()
        self.start_button.draw()
        self.settings_button.draw()
        self.exit_button.draw()