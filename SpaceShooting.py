import pygame,sys
import os

pygame.init()

# constanst values
HEIGHT = 700
WIDTH = 1400

# colors
BG_COLOR = (255,255,255)

# screen display in the game
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SpaceMania')

img1 = pygame.image.load(os.path.join('assets','redship.png'))
img2 = pygame.image.load(os.path.join('assets','blueship.png'))
red = pygame.transform.scale(img1,(85,90))
blue = pygame.transform.scale(img2,(85,90))


def screendis():
    screen.fill( BG_COLOR )
    screen.blit(red,(200,200))
    screen.blit(blue,(900,200))

# the mainloop for game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screendis()
    pygame.display.update()