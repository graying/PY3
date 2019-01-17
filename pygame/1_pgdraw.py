import sys

import pygame as pg
from colors import COLORS


class Bar(object):
    def __init__(self, color_index):
        if color_index + 1 >= len(COLORS):
            color_index = 0
        self.colorIndex = color_index

    def draw(self, my_win):
        my_win.fill(pg.Color(COLORS[self.colorIndex]))

    def next_color(self):
        if self.colorIndex + 1 >= len(COLORS):
            self.colorIndex = 0
        else:
            self.colorIndex += 1


class ColorName(object):
    def __init__(self, color_index):
        if color_index + 1 >= len(COLORS):
            color_index = 0
        self.color_index = color_index

        self.color_name = COLORS[self.color_index]
        self.text_img = my_font.render(self.color_name, True, (0,0,0))

    def draw(self, my_win):
        my_win.blit(self.text_img, (0, 0) )


# return windows size defined from cmd line
def get_win_size():
    if len(sys.argv) < 3:
        return 0, 0
    else:
        return int(sys.argv[1]), int(sys.argv[2])


# init pg
pg.init()

# if winSize is not suitable then using default 800x600
winSize = list(get_win_size())
if winSize[0] == 0 or winSize[1] == 0:
    print("usage: python 1_pgdraw.py x_size y_size, or will be using default size: 800 600")
    winSize[0] = 800
    winSize[1] = 600
win = pg.display.set_mode(winSize)
pg.display.set_caption("drawing... Press ESC to quit")

# my Bar start with index color 100#
myBar = Bar(100)
my_font = pg.font.Font(None, 48)


# content render function, render windows only, no update
def my_render():
    myBar.draw(win)
    myBar.next_color()
    ColorName(myBar.colorIndex).draw(win)


clock = pg.time.Clock()
run = True
while run:
    clock.tick(2)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        run = False
    my_render()
    pg.display.update()

pg.quit()
