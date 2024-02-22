import pygame,sys
import os

pygame.init()

# constanst values
HEIGHT = 700
WIDTH = 1400
SHIP_WIDTH = 85
SHIP_HEIGHT = 90

# colors
BG_COLOR = (255,255,255)

# screen display in the game
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SpaceMania')

img1 = pygame.image.load(os.path.join('assets','redship.png'))
img2 = pygame.image.load(os.path.join('assets','blueship.png'))
red = pygame.transform.scale(img1,(SHIP_WIDTH,SHIP_HEIGHT))
blue = pygame.transform.scale(img2,(SHIP_WIDTH,SHIP_HEIGHT))


def screendis(red_ship,blue_ship):
    screen.fill( BG_COLOR )
    screen.blit(red,(red_ship.x,red_ship.y))
    screen.blit(blue,(blue_ship.x,blue_ship.y))
    pygame.display.update()

# the mainloop for game
def main():
    red_ship = pygame.Rect(200,200,SHIP_WIDTH,SHIP_HEIGHT)
    blue_ship = pygame.Rect(1000,200,SHIP_WIDTH,SHIP_HEIGHT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        red_ship.x += 1
        screendis(red_ship,blue_ship)

    pygame.quit()

if __name__ == "__main__":
    main()
