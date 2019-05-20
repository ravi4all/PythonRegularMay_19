import pygame

# Initialize Pygame
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
white = 255,255,255
black = 0,0,0
color_1 = 100,150,201

sound_1 = pygame.mixer.Sound('bg_music.wav')
sound_1.play(-1)

bgImg = pygame.image.load("img_1.jpg")

def homeScreen():
    font_1 = pygame.font.SysFont(None,80)
    font_2 = pygame.font.SysFont(None, 60)
    text_1 = "Break the Bricks Challenge"
    text_2 = "Press SPACE to Start the Game"
    text_1 = font_1.render(text_1,True,white)
    text_2 = font_2.render(text_2,True,white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        screen.blit(bgImg,(0,0))
        screen.blit(text_1,(100,100))
        screen.blit(text_2,(100,200))
        pygame.display.update()

def gameOver():
    pass

def score(c):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(c), True, red)
    screen.blit(text, (10,10))

def main():
    FPS = 100
    clock = pygame.time.Clock()

    x = (width // 2) - 100
    y = height - 30
    moveX = 0
    ballY = y - 10

    brickWidth = 100
    brickHeight = 25
    rows = 5
    cols = width//brickWidth
    bricks = []
    for i in range(1,rows+1):
        for j in range(cols):
            bricks.append(pygame.Rect(j*(brickWidth+5), i*(brickHeight + 5),brickWidth,brickHeight))
    ballMoveX = 0
    ballMoveY = 0
    ballMove = False
    count = 0
    sound_1.fadeout(5000)
    while True:
        if not ballMove:
            ballX = x + 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 4
                elif event.key == pygame.K_LEFT:
                    moveX = -4
                elif event.key == pygame.K_SPACE:
                    ballMoveY = -4
                    ballMoveX = 4
                    ballMove = True
            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)
        barRect = pygame.draw.rect(screen,black,[x,y,200,20])
        pygame.draw.circle(screen,red,[ballX,ballY],10)
        ballRect = pygame.Rect(ballX, ballY,10,10)

        for i in range(len(bricks)):
            pygame.draw.rect(screen,color_1,bricks[i])

        x += moveX
        ballX += ballMoveX
        ballY += ballMoveY

        for i in range(len(bricks)):
            if bricks[i].colliderect(ballRect):
                ballMoveY = 4
                del bricks[i]
                count += 1
                FPS += 5
                break
        score(count)

        if ballY < 10:
            ballMoveY = 4
        elif ballX < 10:
            ballMoveX = 4
        elif ballX > width - 10:
            ballMoveX = -4
        elif ballRect.colliderect(barRect):
            ballMoveY = -4

        pygame.display.update()
        clock.tick(FPS)
homeScreen()