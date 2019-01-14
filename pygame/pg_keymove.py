import pygame

# init main game window and set title
pygame.init()
dis_x = 800
dis_y = 480
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption("PYGamer~ ESC to quit ...")


# player class initial
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def pos(self):
        return self.x, self.y

    def draw(self, dis):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            dis.blit(walkLeft[self.walkCount // 3], self.pos())
            self.walkCount += 1
        elif self.right:
            dis.blit(walkRight[self.walkCount // 3], self.pos())
            self.walkCount += 1
        else:
            dis.blit(char, self.pos())


clock = pygame.time.Clock()

# load walk left right image from pics folder
walkRight = []
walkLeft = []
leftFileNamePre = 'pics/L'
rightFileNamePre = 'pics/R'
for i in range(1, 10):
    leftFileNameStr = leftFileNamePre + str(i) + '.png'
    walkLeft.append(pygame.image.load(leftFileNameStr))
    rightFileNameStr = rightFileNamePre + str(i) + '.png'
    walkRight.append(pygame.image.load(rightFileNameStr))

# load background and character picture
bg = pygame.image.load('pics/bg.jpg')
char = pygame.image.load('pics/standing.png')


def my_render():
    # draw background
    dis.blit(bg, (0, 0))
    # draw the character
    man.draw(dis)
    # refresh the window content
    pygame.display.update()


man = Player(368, 400, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < dis_x - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.left = man.right = False
        man.walkCount = 0

    if not man.isJump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < dis_y - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.left = right = False
            man.walkCount = 0
            # print("space pressed isJump is:",isJump)
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
            # print("in isJump x and y is:", x, y)
        else:
            man.isJump = False
            man.jumpCount = 10

    my_render()

pygame.quit()
