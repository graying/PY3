import pygame

(width, height) = (1024, 768)
screen = pygame.display.set_mode((width, height))

bg_color = (127, 0, 255)
FPS = 30
screen.fill(bg_color)

pygame.display.set_caption("pygame init window sample")

screen.fill((0,0,0))
clock = pygame.time.Clock()

#All 
all_sprites = pygame.sprite.Group()

running = True
while running:
    # process input
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            running = False

    #update charactors
    all_sprites.update()

    #render all
    clock.tick(FPS)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.flip()

#doesn't need quit() function in new pygame module (v2.0)
#pygame.quit()
