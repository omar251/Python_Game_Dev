import pygame
from rgb import *
import random

def random_loc(x,y):
    rand_loc = [random.randint(0, x), random.randint(0, y)]
    return rand_loc[0],rand_loc[1]

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

