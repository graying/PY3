import pygame, sys
from pygame.locals import *

pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello Pygamer...")
pygame.draw.line(dis, (255,0,255), (0,0), (800,600), 4)
while True:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
