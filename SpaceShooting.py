import pygame,sys
import os
import math

pygame.init()

# constanst values
HEIGHT = 700
WIDTH = 1400
SHIP_WIDTH = 85
SHIP_HEIGHT = 90
VELOCITY = 10
BULLET_VELOCITY = 10
MAX_BULLETS = 4
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BORDER = pygame.Rect(WIDTH/2 - 0.25, 0 , 0.5 , HEIGHT)

RED_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2

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
def screendis(red_ship,blue_ship,red_bullets,blue_bullets):
    # infinite scroll background
    global scroll
    for i in range(0,tiles):
            screen.blit(bg,(i * bg_width + scroll,0))
    scroll -= 3

    if abs(scroll) > bg_width:
         scroll = 0
    # img blit
    pygame.draw.rect(screen,WHITE,BORDER)
    screen.blit(red,(red_ship.x,red_ship.y))
    screen.blit(blue,(blue_ship.x,blue_ship.y))

    for bullet in red_bullets:
         pygame.draw.rect(screen,RED,bullet)
    for bullet in blue_bullets:
         pygame.draw.rect(screen,GREEN,bullet)

    pygame.display.update()


# for the movement of the ship in the screen for red
def red_movement(key_pressed,red_ship):
    if key_pressed[pygame.K_a] and red_ship.x - VELOCITY > 0: #left
         red_ship.x -= VELOCITY
    if key_pressed[pygame.K_d] and red_ship.x + VELOCITY + red_ship.width < BORDER.x - 10 : #right
         red_ship.x += VELOCITY
    if key_pressed[pygame.K_w] and red_ship.y - VELOCITY > 35 : #up
         red_ship.y -= VELOCITY
    if key_pressed[pygame.K_s] and red_ship.y + VELOCITY + red_ship.width < HEIGHT : #down
         red_ship.y += VELOCITY

# for the movement of the ship in the screen for blue
def blue_movement(key_pressed,blue_ship):
    if key_pressed[pygame.K_LEFT] and  blue_ship.x - VELOCITY > BORDER.x + BORDER.width: #left
         blue_ship.x -= VELOCITY
    if key_pressed[pygame.K_RIGHT] and blue_ship.x + VELOCITY + blue_ship.width < WIDTH: #right
         blue_ship.x += VELOCITY
    if key_pressed[pygame.K_UP] and blue_ship.y - VELOCITY  > 35 : #up
         blue_ship.y -= VELOCITY
    if key_pressed[pygame.K_DOWN] and blue_ship.y + VELOCITY + blue_ship.width < HEIGHT: #down
         blue_ship.y += VELOCITY

def bullet_handel(red_ship,blue_ship,red_bullets,blue_bullets):
     for bullet in red_bullets:
          bullet.x += BULLET_VELOCITY
          if blue_ship.colliderect(bullet):
               pygame.event.post(pygame.event.Event(BLUE_HIT))
               red_bullets.remove(bullet)

          elif bullet.x > WIDTH:
               red_bullets.remove(bullet)


     for bullet in blue_bullets:
          bullet.x -= BULLET_VELOCITY
          if red_ship.colliderect(bullet):
               pygame.event.post(pygame.event.Event(RED_HIT))
               blue_bullets.remove(bullet)

          elif bullet.x < 0:
               blue_bullets.remove(bullet)

# the mainloop for game
def main():
    red_ship = pygame.Rect(200,200,SHIP_WIDTH,SHIP_HEIGHT)
    blue_ship = pygame.Rect(1000,200,SHIP_WIDTH,SHIP_HEIGHT)
    red_bullets = []
    blue_bullets = []
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_ship.x + red_ship.width,red_ship.y + red_ship.height//2 - 2, 20 , 3)
                    red_bullets.append(bullet)

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue_ship.x ,blue_ship.y + blue_ship.height//2 - 2, 20 , 3)
                    blue_bullets.append(bullet)

        key_pressed = pygame.key.get_pressed()
        red_movement(key_pressed,red_ship)
        blue_movement(key_pressed,blue_ship)
        screendis(red_ship,blue_ship,red_bullets,blue_bullets)
        bullet_handel(red_ship,blue_ship,red_bullets,blue_bullets)
    pygame.quit()

if __name__ == "__main__":
    main()
