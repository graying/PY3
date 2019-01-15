import sys

import pygame
from colors import COLORS


# return windows size defined from cmd line
def get_win_size():
    if len(sys.argv) < 3:
        return 0, 0
    else:
        return int(sys.argv[1]), int(sys.argv[2])


pygame.init()

# if winSize is not suitable then using default 800x600
winSize = list(get_win_size())
if winSize[0] == 0 or winSize[1] == 0:
    print("parameters parsing error, using default size: 800x600")
    winSize[0] = 800
    winSize[1] = 600
win = pygame.display.set_mode(winSize)
pygame.display.set_caption("drawing... Press ESC to quit")

# graphical content render here
colorIndex = 0
maxColor = len(COLORS)
color = pygame.Color(COLORS[colorIndex])


def my_render():
    win.fill(color)
    pygame.display.update()

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if colorIndex + 1 >= maxColor:
        colorIndex = 0
    else:
        colorIndex += 1
    color = pygame.Color(COLORS[colorIndex])
    my_render()
pygame.quit()
