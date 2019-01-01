import sys

import pygame
import random
from pygame.locals import *

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello PYGamer...")


def rndcolor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_it():
    dis.fill(rndcolor())
    pygame.draw.line(dis, rndcolor(), (0, 0), (800, 600), 4)
    pygame.draw.line(dis, rndcolor(), (800, 0), (0, 600), 5)


draw_it()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            draw_it()
