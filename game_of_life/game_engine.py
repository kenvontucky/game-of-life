from game_of_life.fixtures import CELL, LIMIT


def top(x, y, canvas):
    xx = x - 1
    if xx < 0:
        return False
    return canvas[xx, y] == CELL


def bottom(x, y, canvas):
    xx = x + 1
    if xx > LIMIT:
        return False
    return canvas[xx, y] == CELL


def right(x, y, canvas):
    yy = y + 1
    if yy > LIMIT:
        return False
    return canvas[x, yy] == CELL


def left(x, y, canvas):
    yy = y - 1
    if yy < 0:
        return False
    return canvas[x, yy] == CELL


def top_left(x, y, canvas):
    xx = x - 1
    yy = y - 1
    if xx < 0 or yy < 0:
        return False
    return canvas[xx, yy] == CELL


def top_right(x, y, canvas):
    xx = x - 1
    yy = y + 1
    if xx < 0 or yy > LIMIT:
        return False
    return canvas[xx, yy] == CELL


def bottom_left(x, y, canvas):
    xx = x + 1
    yy = y - 1
    if xx > LIMIT or yy < 0:
        return False
    return canvas[xx, yy] == CELL


def bottom_rigt(x, y, canvas):
    xx = x + 1
    yy = y + 1
    if xx > LIMIT or yy > LIMIT:
        return False
    return canvas[xx, yy] == CELL


def neighbours(x, y, canvas):
    methods = [top, top_left, top_right, right, bottom, bottom_left, bottom_rigt, left]
    check = [f(x, y, canvas) for f in methods]
    return check.count(True)


def alive(x, y, canvas):
    canvas[x, y] = CELL


def dead(x, y, canvas):
    canvas[x, y] = 0


def generation_evaluation(x, y, current_canvas, new_canvas):
    cnt = neighbours(x, y, current_canvas)
    state = current_canvas[x, y]

    if state == 1 and cnt < 2 or cnt > 3:
        dead(x, y, new_canvas)
        return

    if state == 1 and cnt in [2, 3]:
        alive(x, y, new_canvas)
        return

    if state == 0 and cnt == 3:
        alive(x, y, new_canvas)
        return
