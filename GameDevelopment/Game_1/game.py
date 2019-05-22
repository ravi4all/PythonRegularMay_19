import pygame, time
pygame.init()
height = 500
width = 1000
screen = pygame.display.set_mode((width,height))
red = 255,0,0
white = 255,255,255
black = 0,0,0
blue = 0,0,255

bgImage = pygame.image.load("img_1.jpg")
bgMusic = pygame.mixer.Sound('music_1.wav')
bgMusic.play(-1)

def homeScreen():
    msg_1 = "Break The Bricks Challenge"
    msg_2 = "Press SPACE to Start Game"
    # font_1 = pygame.font.SysFont(None,80).render(msg_1,True,white)
    # font_2 = pygame.font.SysFont(None,60).render(msg_2, True, white)
    font_1 = pygame.font.Font('font_1.ttf', 80).render(msg_1, True, white)
    font_2 = pygame.font.Font('zorque.ttf', 60).render(msg_2, True, white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(bgImage,(0,0))
        screen.blit(font_1,(100,100))
        screen.blit(font_2, (100,200))
        pygame.display.update()

def gameOver():
    msg_2 = "Press SPACE to ReStart Game"
    font_2 = pygame.font.Font('zorque.ttf', 40).render(msg_2, True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(font_2, (200, 250))
        pygame.display.update()

def score(counter):
    msg = "Score : {}".format(counter)
    font = pygame.font.SysFont(None, 25)
    text = font.render(msg,True,red)
    screen.blit(text, (10,10))

def life(counter):
    msg = "Life Remaining : {}".format(counter)
    font = pygame.font.SysFont(None, 25)
    text = font.render(msg,True,red)
    screen.blit(text, (300,10))

def game():
    # Bar Variables
    barWidth = 200
    barHeight = 20
    barX = (width//2) - barWidth // 2
    barY = height - barHeight - 10
    moveBarX = 0

    # Ball Variables
    ballRadius = 10
    ballY = barY - ballRadius
    moveBall = False
    moveBallX = 0
    moveBallY = 0

    # Bricks Variables
    brickHeight = 25
    brickWidth = 100
    bricks = []
    rows = 5
    cols = width // brickWidth
    for i in range(1,rows+1):
        for j in range(cols):
            bricks.append(pygame.Rect(j * (brickWidth + 5), i * (brickHeight + 5), brickWidth, brickHeight))
    # print(bricks)
    counter = 0
    lifeRemaining = 3
    FPS = 100
    clock = pygame.time.Clock()
    play = True
    while play:
        if not moveBall:
            ballX = barX + barWidth // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveBarX = 4
                elif event.key == pygame.K_LEFT:
                    moveBarX = -4
                elif event.key == pygame.K_SPACE:
                    moveBall = True
                    moveBallX = 4
                    moveBallY = -4
            elif event.type == pygame.KEYUP:
                moveBarX = 0

        screen.fill(white)
        barRect = pygame.draw.rect(screen,black,[barX,barY,barWidth,barHeight])
        pygame.draw.circle(screen,red,[ballX,ballY],ballRadius)
        ballRect = pygame.Rect(ballX, ballY, ballRadius, ballRadius)
        barX += moveBarX
        ballX += moveBallX
        ballY += moveBallY

        for i in range(len(bricks)):
            pygame.draw.rect(screen, blue, bricks[i])

        for i in range(len(bricks)):
            if bricks[i].colliderect(ballRect):
                moveBallY = 4
                counter += 1
                FPS += 5
                del bricks[i]
                break

        score(counter)
        if ballX < 0:
            moveBallX = 4
        elif ballX > width - ballRadius:
            moveBallX = -4
        elif ballY < 0:
            moveBallY = 4
        elif ballRect.colliderect(barRect):
            moveBallY = -4
        elif ballY > height+height:
            moveBall = False
            ballY = barY - ballRadius
            moveBallY = 0
            moveBallX = 0
            lifeRemaining -= 1

        life(lifeRemaining)
        if lifeRemaining == 0:
            gameOver()
            play = False

        pygame.display.update()
        clock.tick(FPS)

# game()
homeScreen()