import pygame
from rgb import *
import random
from blocks import * 

def random_loc(x,y):
    rand_loc = [random.randint(100, x), random.randint(100, y)]
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

def draw_snake(display,block):
    display.fill(black)
    pygame.draw.rect(display, block.color, (block.X, block.Y, block.W, block.H))
    pygame.display.update()

# def create_child(snake,display):                                                   # [NOT USED]
#     father = snake[len(snake)-1]
#     snake.append(Blocks(father.X-father.W,father.Y,father.W,father.H,father.color,display))
#     return snake

def reset(snake):
    # snake[0].X=250
    # snake[0].Y=250
    for obj in snake[1:]:
        snake.remove(obj)

