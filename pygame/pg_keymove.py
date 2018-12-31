import pygame

pygame.init()

dis_x = 500
dis_y = 500

dis = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption("PYGamer...")

x, y = 50, 400
width = 64
height = 64
vel = 3

isJump = False
jumpCount = 10

left = False
right = False
walkcount = 0

bg = pygame.image.load('pics/bg.jpg')
char = pygame.image.load('pics/standing.png')

# load walk left right image from pics folder
walkRight = []
walkLeft = []
leftFileNamePre = 'pics/L'
rightFileNamePre = 'pics/R'
for i in range(1,9):
    leftFileNameStr = leftFileNamePre+str(i)+'.png'
    walkLeft.append(pygame.image.load(leftFileNameStr))
    rightFileNameStr = rightFileNamePre+str(i)+'.png'
    walkRight.append(pygame.image.load(rightFileNameStr))

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < dis_x - width - vel:
        x += vel

    if not isJump:
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < dis_y - height - vel:
        #     y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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

    dis.fill((0, 0, 0))
    pygame.draw.rect(dis, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
