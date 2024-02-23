import pygame,sys
import os
import math

pygame.init()

# constanst values
HEIGHT = 700
WIDTH = 1400
SHIP_WIDTH = 85
SHIP_HEIGHT = 90
velocity = 5

# clock fps
clock = pygame.time.Clock()
fps = 60

# screen display in the game
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SpaceMania')

# for bg
bg = pygame.image.load(os.path.join('assets','bg.png')).convert()
bg_width = bg.get_width() #for caluclation of the area
scroll = 0 #for looping the image
tiles = math.ceil(WIDTH / bg_width) + 1 # how many bg needed in the screen # +1 is for buffer

# getting images
img1 = pygame.image.load(os.path.join('assets','redship.png'))
img2 = pygame.image.load(os.path.join('assets','blueship.png'))

# scaling the image in right size
red = pygame.transform.scale(img1,(SHIP_WIDTH,SHIP_HEIGHT))
blue = pygame.transform.scale(img2,(SHIP_WIDTH,SHIP_HEIGHT))



# for screen dislay
def screendis(red_ship,blue_ship):
    # infinite scroll background
    global scroll
    for i in range(0,tiles):
            screen.blit(bg,(i * bg_width + scroll,0))
    scroll -= 3

    if abs(scroll) > bg_width:
         scroll = 0
    # img blit
    screen.blit(red,(red_ship.x,red_ship.y))
    screen.blit(blue,(blue_ship.x,blue_ship.y))
    pygame.display.update()


# for the movement of the ship in the screen for red
def red_movement(key_pressed,red_ship):
    if key_pressed[pygame.K_a]: #left
         red_ship.x -= velocity
    if key_pressed[pygame.K_d]: #right
         red_ship.x += velocity
    if key_pressed[pygame.K_w]: #up
         red_ship.y -= velocity
    if key_pressed[pygame.K_s]: #down
         red_ship.y += velocity

# for the movement of the ship in the screen for blue
def blue_movement(key_pressed,blue_ship):
    if key_pressed[pygame.K_LEFT]: #left
         blue_ship.x -= velocity
    if key_pressed[pygame.K_RIGHT]: #right
         blue_ship.x += velocity
    if key_pressed[pygame.K_UP]: #up
         blue_ship.y -= velocity
    if key_pressed[pygame.K_DOWN]: #down
         blue_ship.y += velocity



# the mainloop for game
def main():
    red_ship = pygame.Rect(200,200,SHIP_WIDTH,SHIP_HEIGHT)
    blue_ship = pygame.Rect(1000,200,SHIP_WIDTH,SHIP_HEIGHT)
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        red_movement(key_pressed,red_ship)
        blue_movement(key_pressed,blue_ship)
        screendis(red_ship,blue_ship)
    pygame.quit()

if __name__ == "__main__":
    main()
