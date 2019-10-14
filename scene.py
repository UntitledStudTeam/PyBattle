import pyglet
import utils
from grid_hexagon import HexagonalGrid
import settings
import time


class GameScene:
    def __init__(self,width,height):
        self.goto = GameScene
        self.grid = HexagonalGrid(width, height, 30, 20)
        self.game_time = time.time()
        self.batch = pyglet.graphics.Batch()
        pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)

        points = []
        colors = []
        vertices_count = (self.grid.mapping_grid_height + 1) * (self.grid.mapping_grid_width + 1)
        for y in range(self.grid.mapping_grid_height + 1):
            for x in range(self.grid.mapping_grid_width + 1):
                points.extend(self.grid.get_index_position(x, y))
                colors.extend([255] * 3)

        self.batch.add(vertices_count, pyglet.gl.GL_POINTS, None, ('v2i', points), ('c3B', colors))

        # draw centers

        centers = []
        colors = []
        centers_count = self.grid.map_width * self.grid.map_height
        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                centers.extend(self.grid.get_hex_center(x, y))
                colors.extend([255, 0, 0])

        self.batch.add(centers_count, pyglet.gl.GL_POINTS, None, ('v2i', centers), ('c3B', colors))

        # draw_lines

        for y in range(self.grid.map_height):
            for x in range(self.grid.map_width):
                self.batch.add(12, pyglet.gl.GL_LINES, None, ('v2i', self.grid.get_hex_lines(x, y)),
                               ('c3B', [0, 255, 0] * 12))

    def on_mouse_press(self):
        self.goto = MenuScene

    def on_draw(self):
        self.batch.draw()
        time_label = "{:2.2f}".format(time.time() - self.game_time)
        time_label = pyglet.text.Label(time_label, font_size=20, x=1000, y=10, color=(255,255,255,255))
        time_label.draw()

class MenuScene:
    def __init__(self,width,height):
        self.goto = MenuScene
        self.label = pyglet.text.Label('PyBattle', font_name='Times New Roman',
                          font_size=36, x=200, y=200,
                          anchor_x='center', anchor_y='center', color=(1,0,0,255))
        pyglet.gl.glClearColor(176/255, 220/255, 112/255, 1)

    def on_mouse_press(self):
        self.goto = GameScene

    def on_draw(self):
        self.label.draw()
