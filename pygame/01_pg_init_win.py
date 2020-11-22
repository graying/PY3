import pygame

(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))

bg_color = (127, 0, 255)
screen.fill(bg_color)

pygame.display.set_caption("pygame init window sample")

screen.fill((0,0,0))

running = True
while running:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()

#pygame.quit()
