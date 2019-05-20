import pygame
pygame.init()
height = 500
width = 1000
screen = pygame.display.set_mode((width,height))
red = 255,0,0
white = 255,255,255
black = 0,0,0

screen.fill(white)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()