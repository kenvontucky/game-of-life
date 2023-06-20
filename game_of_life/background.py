import random

import pyxel

from fixtures import FPS


class Background:
    def __init__(self):
        self.star_list = []
        self.starcount = 80
        self.star_color_high = 7
        self.star_color_low = 13
        for i in range(self.starcount):
            self.star_list.append(
                (random.random() * pyxel.width, random.random() * pyxel.height, random.random() * 1.5 + 1)
            )

    def update(self):
        for i, (x, y, speed) in enumerate(self.star_list):
            if FPS != 0:
                x -= speed * 30 / FPS
            if x <= 0:
                x += pyxel.width
            self.star_list[i] = (x, y, speed)

    def draw(self):
        for x, y, speed in self.star_list:
            pyxel.pset(x, y, self.star_color_high if speed > 1.8 else self.star_color_low)
