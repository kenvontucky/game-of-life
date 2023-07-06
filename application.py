from time import time
import pyxel

from game_of_life.background import Background
from game_of_life.game_engine import generation_evaluation
from game_of_life.fixtures import A, B, C, CELL, D, DELAY, E, FPS, G, H, I, K, L, M, MAXIMUM, N, O, R, S, T, U, V, W


class App:
    current_canvas = [[0 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]
    next_canvas = [[0 for _ in range(MAXIMUM)] for _ in range(MAXIMUM)]

    def __init__(self):
        self.start_time = time()
        pyxel.init(MAXIMUM, MAXIMUM, fps=FPS)

        self.initial_cells()
        self.background = Background()

        pyxel.run(self.update, self.draw)

    def initial_cells(self):
        self.render_letters(20, [W, E, L, C, O, M, E])

    def render_letters(self, y_offset, letters):
        m = 0
        for item in letters:
            y = y_offset
            for letter in item:
                x = 5 + m
                for value in letter:
                    if value == CELL:
                        self.current_canvas[x][y] = CELL
                    x += 1
                y += 1
            m += 8

    def update(self):
        if int(time() - self.start_time) >= DELAY:
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
