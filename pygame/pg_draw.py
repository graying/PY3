import pygame, sys, random
from pygame.locals import *

pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello Pygamer...")
def rndColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def draw_it():
    dis.fill(rndColor())
    pygame.draw.line(dis, rndColor(), (0,0), (800,600), 4)
    pygame.draw.line(dis, rndColor(), (800,0), (0,600), 5)

draw_it()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            draw_it()
