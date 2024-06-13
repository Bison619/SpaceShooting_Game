import pygame
import sys
import os
import math
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


pygame.mixer.music.load(os.path.join('assets/bg space music.mp3'))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# constanst values
HEIGHT = 700
WIDTH = 1400
SHIP_WIDTH = 85
SHIP_HEIGHT = 90
VELOCITY = 10
BULLET_VELOCITY = 20
MAX_BULLETS = 5
HEALTH_FONT = pygame.font.SysFont("Comicsans",30)
WINNER_FONT = pygame.font.SysFont("Comicsans",120)
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets/fire.mp3'))

# colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BORDER = pygame.Rect(WIDTH/2 - 0.25, 0 , 0.5 , HEIGHT)

# events for hit
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
def screendis(red_ship,blue_ship,red_bullets,blue_bullets, RED_HEALTH, BLUE_HEALTH):
    # infinite scroll background
    global scroll
    for i in range(0,tiles):
            screen.blit(bg,(i * bg_width + scroll,0))
    scroll -= 3

    if abs(scroll) > bg_width:
         scroll = 0
    # img blit
    pygame.draw.rect(screen,WHITE,BORDER)
    red_health_text = HEALTH_FONT.render("Health : " + str(RED_HEALTH),1, WHITE )
    blue_health_text = HEALTH_FONT.render("Health : " + str(BLUE_HEALTH),1, WHITE )
    screen.blit(red_health_text, (WIDTH - red_health_text.get_width() -10 ,10))
    screen.blit(blue_health_text, (10 ,10))
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
    if key_pressed[pygame.K_w] and red_ship.y - VELOCITY > 40 : #up
         red_ship.y -= VELOCITY
    if key_pressed[pygame.K_s] and red_ship.y + VELOCITY + red_ship.width < HEIGHT : #down
         red_ship.y += VELOCITY

# for the movement of the ship in the screen for blue
def blue_movement(key_pressed,blue_ship):
    if key_pressed[pygame.K_LEFT] and  blue_ship.x - VELOCITY > BORDER.x + BORDER.width: #left
         blue_ship.x -= VELOCITY
    if key_pressed[pygame.K_RIGHT] and blue_ship.x + VELOCITY + blue_ship.width < WIDTH: #right
         blue_ship.x += VELOCITY
    if key_pressed[pygame.K_UP] and blue_ship.y - VELOCITY  > 40 : #up
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

def winner_text(text):
     text_draw = WINNER_FONT.render(text,1,WHITE)
     screen.blit (text_draw, (WIDTH/2 -text_draw.get_width()/2,HEIGHT/2-text_draw.get_height()/2))
     pygame.display.update()
     pygame.time.delay(3000)



# the mainloop for game
def main():
    red_ship = pygame.Rect(200,200,SHIP_WIDTH,SHIP_HEIGHT)
    blue_ship = pygame.Rect(1000,200,SHIP_WIDTH,SHIP_HEIGHT)
    red_bullets = []
    blue_bullets = []
    RED_HEALTH = 100
    BLUE_HEALTH = 100
    BULLET_HIT_SOUND = pygame.mixer.Sound('assets/hit.mp3')
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_ship.x + red_ship.width,red_ship.y + red_ship.height//2 - 2, 20 , 3)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue_ship.x ,blue_ship.y + blue_ship.height//2 - 2, 20 , 3)
                    blue_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                 BLUE_HEALTH -= 10
                 BULLET_HIT_SOUND.play()

            if event.type == BLUE_HIT:
                 RED_HEALTH -= 10
                 BULLET_HIT_SOUND.play()

        WINNER = ""
        if RED_HEALTH <= 0 :
             WINNER = "RED WON..!!"

        if BLUE_HEALTH <=0 :
             WINNER = "BLUE WON..!!"

        if WINNER != "":
             winner_text(WINNER)
             break
        key_pressed = pygame.key.get_pressed()
        red_movement(key_pressed,red_ship)
        blue_movement(key_pressed,blue_ship)
        screendis(red_ship,blue_ship,red_bullets,blue_bullets,RED_HEALTH,BLUE_HEALTH)
        bullet_handel(red_ship,blue_ship,red_bullets,blue_bullets)
    main()

if __name__ == "__main__":
    main()

