import pygame, sys
from pygame.locals import *

pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello Pygamer...")
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
