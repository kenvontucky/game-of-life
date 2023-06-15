from game_of_life.base import CELL, MAXIMUM, generation_evaluation
import pyxel
import numpy as np


class App:
    current_canvas = np.zeros((MAXIMUM,MAXIMUM))
    next_canvas = np.zeros((MAXIMUM,MAXIMUM))

    def __init__(self):
        self.initial_cells()
        pyxel.init(MAXIMUM, MAXIMUM)
        pyxel.run(self.update, self.draw)

    def initial_cells(self):
        self.current_canvas[0,1]=1
        self.current_canvas[1,2]=1
        self.current_canvas[2,0]=1
        self.current_canvas[2,1]=1
        self.current_canvas[2,2]=1

    def update(self):
        for x in range(MAXIMUM):
            for y in range(MAXIMUM):
                generation_evaluation(x,y, self.current_canvas, self.next_canvas)

        self.current_canvas = self.next_canvas
        self.next_canvas = np.zeros((MAXIMUM,MAXIMUM))

    def draw(self):
        pyxel.cls(0)

        for x in range(MAXIMUM):
            for y in range(MAXIMUM):
                if self.current_canvas[x,y] == CELL:
                    pyxel.rect(x, y, 1, 1, 9)


App()
