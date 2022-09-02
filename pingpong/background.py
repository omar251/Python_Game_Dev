import pygame
from rgb import *

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
    ball.dx,ball.dy = direct[random.randint(0, 1)],ball.ball_speed#*direct[random.randint(0, 1)]
    ball.score = 0
    
