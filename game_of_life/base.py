import numpy as np
from time import sleep

CELL = 1
MAXIMUM = 9
LIMIT = MAXIMUM - 1

canvas = np.zeros((MAXIMUM, MAXIMUM))
next_canvas = np.zeros((MAXIMUM, MAXIMUM))


def top(x, y):
    xx = x - 1
    if xx < 0:
        return False
    return canvas[xx, y] == CELL


def bottom(x, y):
    xx = x + 1
    if xx > LIMIT:
        return False
    return canvas[xx, y] == CELL


def right(x, y):
    yy = y + 1
    if yy > LIMIT:
        return False
    return canvas[x, yy] == CELL


def left(x, y):
    yy = y - 1
    if yy < 0:
        return False
    return canvas[x, yy] == CELL


def top_left(x, y):
    xx = x - 1
    yy = y - 1
    if xx < 0 or yy < 0:
        return False
    return canvas[xx, yy] == CELL


def top_right(x, y):
    xx = x - 1
    yy = y + 1
    if xx < 0 or yy > LIMIT:
        return False
    return canvas[xx, yy] == CELL


def bottom_left(x, y):
    xx = x + 1
    yy = y - 1
    if xx > LIMIT or yy < 0:
        return False
    return canvas[xx, yy] == CELL


def bottom_rigt(x, y):
    xx = x + 1
    yy = y + 1
    if xx > LIMIT or yy > LIMIT:
        return False
    return canvas[xx, yy] == CELL


def neighbours(x, y):
    methods = [top, top_left, top_right, right, bottom, bottom_left, bottom_rigt, left]
    check = [f(x, y) for f in methods]
    return check.count(True)


def alive(x, y):
    next_canvas[x, y] = CELL


def dead(x, y):
    next_canvas[x, y] = 0


def generation_evaluation(x, y):
    cnt = neighbours(x, y)
    state = canvas[x, y]

    if state == 1 and cnt < 2 or cnt > 3:
        dead(x, y)
        return

    if state == 1 and cnt in [2, 3]:
        alive(x, y)
        return

    if state == 0 and cnt == 3:
        alive(x, y)
        return
