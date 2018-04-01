__author__ = 'swapn'
import pygame
import random
pygame.init()
size = width, height = 800, 600
clock = pygame.time.Clock()
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

gameExit = False
paddle1 = pygame.Rect(5, height/2, 15, 60)
paddle2 = pygame.Rect(width-20, height/2, 15, 60)

scoreP1 = 0
scoreP2 = 0

middleline = pygame.Rect(width/2, 0, 3, height)
ballrect = pygame.Rect(width/2, height/2, 40, 40)
ballPic = pygame.image.load("ball.png")
ballPic = pygame.transform.scale(ballPic, (40, 40))
speed = [1, 1]
font = pygame.font.SysFont(None, 50)


def messageOnScreen(msg, x, y, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [x, y])

menuExit = False
while not menuExit:
    gameDisplay.fill((0, 0, 0))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    messageOnScreen("Pong!", 350, 20, (255, 255, 255))
    play = pygame.Rect(200, 150, 400, 80)
    pygame.draw.rect(gameDisplay, (57, 168, 116), play)
    gameDisplay.blit(font.render("Play", True, (255, 255, 255)), (360, 170))
    click = pygame.mouse.get_pressed()
    if 600 > pos[0] > 200 and 230 > pos[1] > 150 and click[0] == 1:
        menuExit = True
    pygame.display.update()


while True:
    ballrect.x = random.randrange(300, 500)
    ballrect.y = random.randrange(200, 400)
    gameExit = False

    pygame.time.wait(100)

    if scoreP1 > 9 or scoreP2 > 9:
        break

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and paddle1.y < 540:
            paddle1 = paddle1.move(0, 1)
        elif keys[pygame.K_w] and paddle1.y > 0:
            paddle1 = paddle1.move(0, -1)

        if keys[pygame.K_DOWN] and paddle2.y < 540:
            paddle2 = paddle2.move(0, 1)
        elif keys[pygame.K_UP] and paddle2.y > 0:
            paddle2 = paddle2.move(0, -1)
        ballrect = ballrect.move(speed)

        if paddle1.colliderect(ballrect) or paddle2.colliderect(ballrect):
            speed[0] = -speed[0]

        if ballrect.left < 0:
            scoreP1 += 1
    #        speed[0] = -speed[0]
            gameExit = True
        if ballrect.right > width:
            scoreP2 += 1
    #        speed[0] = -speed[0]
            gameExit = True
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        gameDisplay.fill((57, 168, 116))
        messageOnScreen(str(scoreP2), width/2-40, 10, (0, 0, 0))
        messageOnScreen(str(scoreP1), width/2+20, 10, (0, 0, 0))
        pygame.draw.rect(gameDisplay, black, paddle1)
        pygame.draw.rect(gameDisplay, black, paddle2)
        pygame.draw.rect(gameDisplay, black, middleline)
        gameDisplay.blit(ballPic, ballrect)
        clock.tick(400)
        pygame.display.update()

    #gameExit = False

if scoreP1 > scoreP2:
    messageOnScreen("Player 1 Won!", 300, 300, (255, 255, 255))
else:
    messageOnScreen("Player 2 Won!", 300, 300, (255, 255, 255))
pygame.display.update()

pygame.time.wait(3000)


pygame.quit()
quit()