import pyxel

from background import Background
from game_engine import generation_evaluation
from fixtures import CELL, FPS, MAXIMUM


class App:
    current_canvas = [[0 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]
    next_canvas = [[0 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]

    def __init__(self):
        pyxel.init(MAXIMUM, MAXIMUM, fps=FPS)

        self.initial_cells()
        self.background = Background()

        pyxel.run(self.update, self.draw)

    def initial_cells(self):
        self.current_canvas[0][1] = 1
        self.current_canvas[1][2] = 1
        self.current_canvas[2][0] = 1
        self.current_canvas[2][1] = 1
        self.current_canvas[2][2] = 1

    def update(self):
        for x in range(MAXIMUM):
            for y in range(MAXIMUM):
                generation_evaluation(x, y, self.current_canvas, self.next_canvas)

        self.current_canvas = self.next_canvas
        self.next_canvas = [[0 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]

        self.background.update()

    def draw(self):
        pyxel.cls(0)

        for x in range(MAXIMUM):
            for y in range(MAXIMUM):
                if self.current_canvas[x][y] == CELL:
                    pyxel.rect(x, y, 1, 1, 9)

        self.background.draw()


App()
