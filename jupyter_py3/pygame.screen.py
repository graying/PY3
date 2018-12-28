import random
import time

import pygame

pygame.init()
screen = pygame.display.set_mode([1440, 900])
screen.fill([0, 0, 0])

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

rectcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
rectsize = [random.randint(0, 1000), random.randint(0, 900), random.randint(0, 256), random.randint(0, 256)]
pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0, 5))
pygame.display.flip()

for i in range(100):
    rectcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    rectsize = [random.randint(0, 1220), random.randint(0, 800), random.randint(0, 256), random.randint(0, 256)]
    pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0, 5))
    pygame.display.update()
    fpsClock.tick(FPS)
    time.sleep(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
