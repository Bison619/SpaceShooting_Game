import pygame,sys
import numpy as np

pygame.init()

# constanst values
HEIGHT = 600
WIDTH = 600
LINE_WIDTH = 15
RADIUS = 60
C_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
# colors
BG_COLOR = (216, 134, 235)
LINE_COLOR = (37, 22, 41)
C_COLOR = (255,255,255)
WIN_C = (255,0,0)

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
                pygame.draw.circle( screen,LINE_COLOR, (int(col*200+200/2),int(row*200+200/2)),RADIUS,C_WIDTH)
            elif board [row][col] == 2:
                pygame.draw.line(screen,C_COLOR,(col*200+SPACE,row*200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), CROSS_WIDTH )
                pygame.draw.line(screen,C_COLOR,(col*200+SPACE,row*200+SPACE), (col*200+200-SPACE, row*200+200-SPACE), CROSS_WIDTH )


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

def check_game(player):
    # for the vertical cross in the game
    for col in range(3):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_verticalline(col,player)
            return True
    # for the horzontal
    for row in range(3):
        if board[row][0]==player and board[row][1] ==player and board[row][2]==player:
            draw_horizontal(row,player)
            return True
    # for diagonal and ascending one
    if board[2][0] ==player and board[1][1] ==player and board[0][2]==player:
        draw_acsver(player)
        return True
    # for diagonal and descending one
    if board [0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_decsver(player)
        return True
    return False

def draw_verticalline(col,player):
    posx = col * 200 + 100
    if player == 1:
        Win=WIN_C
    elif player== 2:
        Win=WIN_C
    pygame.draw.line(screen,Win,(posx,15),(posx-HEIGHT-15),15)
def draw_horizontal(row,player):
    pass
def draw_acsver(player):
    pass
def draw_decsver(player):
    pass

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
                    check_game(player)
                    player = 2
                elif player == 2 :
                    marked_sq(clicked_row, clicked_col, 2)
                    check_game(player)
                    player  = 1

                draw_shape()


    pygame.display.update()