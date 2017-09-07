import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 760

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

transpongboard = pygame.image.load('C:/Users/techa/PycharmProjects/Test/transpongboard.png')
pongboard2 = pygame.image.load('C:/Users/techa/PycharmProjects/Test/transpongboard2.png')


def ball(ballx, bally, ballw, ballh, ballcolor):
    pygame.draw.rect(gameDisplay, ballcolor, [ballx, bally, ballw, ballh])


def pongboard(x, y):
    gameDisplay.blit(transpongboard, (x, y))


def pongboardtwo(x2, y2):
    gameDisplay.blit(pongboard2, (x2, y2))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 36)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)


def lose1():
    message_display('Player 2 Wins!')
    game_loop()


def lose2():
    message_display('Player 1 Wins!')
    game_loop()


def lose12():
    message_display('Player 2 Wins!')
    game_loop2()


def lose22():
    message_display('Player 1 Wins!')
    game_loop2()


def game_loop():  # This is for two player
    x = (display_width * 0.05)
    y = (display_height * .4)
    x2 = (display_width * .95)
    y2 = (display_height * .4)

    y_change = 0
    y2_change = 0

    ball_startx = display_width / 2
    ball_starty = random.randrange(0, display_height - 51)
    ball_speedx = random.randrange(-5, 6, 10)
    ball_speedy = random.randrange(-5, 6, 2)
    ball_width = 50
    ball_height = 50

    over = False

    while not over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    y_change = 3
                elif event.key == pygame.K_w:
                    y_change = -3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y2_change = 3

                elif event.key == pygame.K_UP:
                    y2_change = -3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y2_change = 0

        y += y_change
        y2 += y2_change

        gameDisplay.fill(black)

        ball(ball_startx, ball_starty, ball_width, ball_height, white)

        if ball_starty >= display_height - 50 or ball_starty <= 0:
            ball_speedy = -ball_speedy

        if ball_startx == x + 25:
            if ball_starty > (y - 50) and ball_starty < y + 192:
                ball_speedx = -ball_speedx
                if y_change > 0:
                    if ball_speedy > 0:
                        ball_speedy += .5
                if y_change < 0:
                    if ball_speedy < 0:
                        ball_speedy += -.5

        elif ball_startx == x2 - 50:
            if ball_starty > (y2 - 50) and ball_starty < y2 + 192:
                ball_speedx = -ball_speedx
                if ball_speedy < 8 or ball_speedy > -8:
                    if y_change > 0:
                        if ball_speedy > 0:
                            ball_speedy += .5
                    if y_change < 0:
                        if ball_speedy < 0:
                            ball_speedy += -.5
                elif ball_speedy == 5 or ball_speedy == -5:
                    if ball_speedx > 0:
                        ball_speedx += .5
                    if ball_speedx < 0:
                        ball_speedx += -.5

        elif ball_startx < x:
            lose1()

        elif ball_startx > x2:
            lose2()

        ball_starty += ball_speedy
        ball_startx += ball_speedx

        pongboard(x, y)
        pongboardtwo(x2, y2)

        if y > display_height - 140:
            y = -50
        elif y < -50:
            y = display_height - 142

        if y2 > display_height - 140:
            y2 = -50
        elif y2 < -50:
            y2 = display_height - 142

        pygame.display.update()
        clock.tick(60)

    while over:
        pygame.quit()
        quit()


def game_loop2():  # This is for single player
    x = (display_width * 0.05)
    y = (display_height * .4)
    x2 = (display_width * .95)
    y2 = (display_height * .4)

    y_change = 0
    y2_change = 0

    ball_startx = display_width / 2
    ball_starty = random.randrange(0, display_height - 51)
    ball_speedx = random.randrange(-5, 6, 10)
    ball_speedy = random.randrange(-5, 6, 2)
    ball_width = 50
    ball_height = 50

    over = False

    while not over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = 3
                elif event.key == pygame.K_UP:
                    y_change = -3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        if ball_starty > (y2 + 60):
            if y2 > display_height - 180:
                y2_change = 0
            else:
                y2_change = 3
        elif ball_starty < y2 + 50:
            if y2 < -20:
                y2_change = 0
            else:
                y2_change = -3
        else:
            y2_change = 0

        y += y_change
        y2 += y2_change

        gameDisplay.fill(black)

        ball(ball_startx, ball_starty, ball_width, ball_height, white)

        if ball_starty >= display_height - 50 or ball_starty <= 0:
            ball_speedy = -ball_speedy

        if ball_startx == x + 25:
            if ball_starty > (y - 50) and ball_starty < y + 192:
                ball_speedx = -ball_speedx
                if y_change > 0:
                    if ball_speedy > 0:
                        ball_speedy += .5
                if y_change < 0:
                    if ball_speedy < 0:
                        ball_speedy += -.5

        elif ball_startx == x2 - 50:
            if ball_starty > (y2 - 50) and ball_starty < y2 + 192:
                ball_speedx = -ball_speedx
                if ball_speedy < 8 or ball_speedy > -8:
                    if y_change > 0:
                        if ball_speedy > 0:
                            ball_speedy += .5
                    if y_change < 0:
                        if ball_speedy < 0:
                            ball_speedy += -.5
                elif ball_speedy == 5 or ball_speedy == -5:
                    if ball_speedx > 0:
                        ball_speedx += .5
                    if ball_speedx < 0:
                        ball_speedx += -.5

        elif ball_startx < x:
            lose12()

        elif ball_startx > x2:
            lose22()

        ball_starty += ball_speedy
        ball_startx += ball_speedx

        pongboard(x, y)
        pongboardtwo(x2, y2)

        if y > display_height - 140:
            y = -50
        elif y < -50:
            y = display_height - 142

        if y2 > display_height - 140:
            y2 = -50
        elif y2 < -50:
            y2 = display_height - 142

        pygame.display.update()
        clock.tick(60)

    while over:
        pygame.quit()
        quit()


vs_ai = input("# of Players: ")

if vs_ai == "2":
    game_loop()
elif vs_ai == "1":
    game_loop2()
else:
    message_display("Please Restart And Enter \"1\" or \"2\"")

pygame.quit()
quit()