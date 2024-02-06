import pygame,sys

pygame.init()

# constansts
HEIGHT = 600
WIDTH = 600
LINE_WIDTH = 15

# colors
BG_COLOR = (216, 134, 235)
LINE_COLOR = (37, 22, 41)

screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('TicTacToe Game')
screen.fill( BG_COLOR )

# horizontal lines
pygame.draw.line(screen,LINE_COLOR,(20,200), (580,200) ,LINE_WIDTH)
pygame.draw.line(screen,LINE_COLOR,(20,400), (580,400) ,LINE_WIDTH)
# vertical lines
pygame.draw.line(screen,LINE_COLOR,(200,20),(200,580),LINE_WIDTH)
pygame.draw.line(screen,LINE_COLOR,(400,20),(400,580),LINE_WIDTH)

# the mainloop for game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    pygame.display.update()