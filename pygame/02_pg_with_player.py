import pygame, random

(WIDTH, HEIGHT) = (800, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_color = (0, 0, 255)
FPS = 60
pygame.display.set_caption("pygame init window sample")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x=WIDTH-50
        self.rect.y=HEIGHT-50
        #self.x = random.randint(0, WIDTH)
        #self.y = random.randint(0, HEIGHT)

    def update(self):
        self.rect.x += 4
        self.rect.y -= 3
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = HEIGHT

#all sprites in the group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Initial and render at first
screen.fill(bg_color)
all_sprites.draw(screen)
pygame.display.flip()


running = True
while running:
    # process input
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            running = False

    #update 
    all_sprites.update()

    #render 
    clock.tick(FPS)
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()

#doesn't need quit() function in new pygame module (v2.0)
#pygame.quit()
