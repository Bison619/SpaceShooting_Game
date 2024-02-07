import pygame,sys
import numpy as np

pygame.init()

# constanst values
HEIGHT = 600
WIDTH = 600
LINE_WIDTH = 15

# colors
BG_COLOR = (216, 134, 235)
LINE_COLOR = (37, 22, 41)

screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('TicTacToe Game')
screen.fill( BG_COLOR )

board = np.zeros((3,3))
print(board)

def draw_line():
    # horizontal lines
    pygame.draw.line(screen,LINE_COLOR,(20,200), (580,200) ,LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(20,400), (580,400) ,LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen,LINE_COLOR,(200,20),(200,580),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,20),(400,580),LINE_WIDTH)


def draw_shape ():
    for row in range(3):
        for col in range(3):
            if board [row][col]==1:
                pass
            elif board [row][col] == 2:
                pass

def marked_sq(row, col, player):
    board[row][col] = player

def available_sq(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False

    return True

draw_line()

player = 1


# the mainloop for game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0] #for xaxis
            mousey = event.pos[1] #for yaxis

            clicked_row = int(mousey//200)  #rounding up the number to smaller one
            clicked_col = int(mousex//200)

            if available_sq(clicked_row,clicked_col):
                if player == 1 :
                    marked_sq(clicked_row,clicked_col,1)
                    player = 2
                elif player == 2 :
                    marked_sq(clicked_row, clicked_col, 2)
                    player  = 1

                draw_shape()


    pygame.display.update()