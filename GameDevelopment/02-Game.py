import pygame

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))

red = 255,0,0
white = 255,255,255
black = 0,0,0
color_1 = 100,150,201
screen.fill(white)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen, color, [x,y,w,h]
    pygame.draw.rect(screen,red,[100,100,50,50])
    pygame.draw.circle(screen, red, [250,250],80)

    pygame.display.update()