import pygame
from rgb import *
from blocks import *

def write_score(display,eaten):
    myfont = pygame.font.SysFont('Comic Sans MS', 16, True)
    score = myfont.render('score '+str(eaten), False, white)
    display.blit(score, (380, 5))
    pygame.display.update()

def write_stuff(display, string, size, color, p_x, p_y):
    da_font = pygame.font.SysFont('Comic Sans MS', size, True)
    word = da_font.render(str(string), False, color)
    display.blit(word, (p_x, p_y))
    pygame.display.update()


def reset(ball):
    ball.X,ball.Y= ball.centerX ,ball.centerY
    direct=[2.5,-2.5]
    ball.dx,ball.dy = 0,ball.ball_speed #direct[random.randint(0, 1)],ball.ball_speed
    ball.score = 0
    
def create_bricks(display,row,next_row):
    last_block = row[len(row)-1]
    if last_block.Y >=last_block.display.get_height() :
        return next_row
    else:
        if last_block.X >=last_block.display.get_width()- 40 :
            next_row += 1
            row.append(Blocks(row[0].X,(last_block.H * next_row),last_block.W,last_block.H,rand_color(),display))
            return next_row
        else:
            row.append(Blocks(last_block.X + last_block.W,last_block.Y,last_block.W,last_block.H,rand_color(),display))
            return next_row
