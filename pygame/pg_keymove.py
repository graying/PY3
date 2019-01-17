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
        self.standing = True

    def pos(self):
        return self.x, self.y

    def draw(self, mydis):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                mydis.blit(walkLeft[self.walkCount // 3], self.pos())
                self.walkCount += 1
            elif self.right:
                mydis.blit(walkRight[self.walkCount // 3], self.pos())
                self.walkCount += 1
        else:
            if self.left:
                mydis.blit(walkLeft[0], self.pos())
            else:
                mydis.blit(walkRight[0], self.pos())


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def pos(self):
        return self.x, self.y

    def draw(self, mydis):
        pygame.draw.circle(mydis, self.color, self.pos(), self.radius)


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
    for bullet in bullets:
        bullet.draw(dis)
    # refresh the window content
    pygame.display.update()


man = Player(368, 400, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if dis_x > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) <= 5:
            bullets.append(Projectile(round(man.x + man.width // 2),
                                      round(man.y + man.height // 2), 6, (0, 0, 0), facing))
    elif keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < dis_x - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < dis_y - height - vel:
        #     y += vel
        if keys[pygame.K_UP]:
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
