import pygame

pygame.init()

# init main game window and set title
dis_x = 500
dis_y = 500
dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption("PYGamer...")

clock = pygame.time.Clock()
x, y = 50, 350
width = 64
height = 64
vel = 3

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

bg = pygame.image.load('pics/bg.jpg')
char = pygame.image.load('pics/standing.png')

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


def myRender():
    global walkCount
    dis.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        dis.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        dis.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        dis.blit(char, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < dis_x - width - vel:
        x += vel
        right = True
        left = False
    else:
        left = right = False
        walkCount = 0

    if not isJump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < dis_y - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            left = right = False
            walkCount = 0
            # print("space pressed isJump is:",isJump)
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            print("in isJump x and y is:", x, y)
        else:
            isJump = False
            jumpCount = 10

    myRender()

pygame.quit()
