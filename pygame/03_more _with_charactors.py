import pygame, random, os

(WIDTH, HEIGHT) = (800, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_color = "BLACK"
FPS = 60

#images files are stored in img folder within game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#set the file name as the title of the window
pygame.display.set_caption(os.path.basename(__file__))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img_path = os.path.join(img_folder, "p2_walk01.png")
        self.image = pygame.image.load(img_path).convert()
        self.image.set_colorkey("BLACK")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT/2
        self.y_speed = 3

    def update(self):
        self.rect.x += 4
        self.rect.y += self.y_speed
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.bottom > HEIGHT-100:
            self.y_speed = -3
        if self.rect.top < 100:
            self.y_speed = 3

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
        #print (event)
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
