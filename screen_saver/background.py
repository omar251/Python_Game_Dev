import pygame
from rgb import *
import random
from blocks import * 

def random_loc(x,y):
    rand_loc = [random.randint(0, x), random.randint(0, y)]
    return rand_loc[0],rand_loc[1]

def draw_screen(display,list):
    display.fill(black)
    for obj in list:
        obj.draw_block(display)
    pygame.display.update()

def create_row(display,row,next_row):
    last_block = row[len(row)-1]
    if last_block.Y >=500 :
        return next_row
    else:
        if last_block.X >=500 :
            next_row += 1
            row.append(Blocks(0,(last_block.H * next_row),last_block.W,last_block.H,rand_color(),display))
            print(last_block.X,last_block.Y,last_block.W,last_block.H,next_row)
            return next_row
        else:
            row.append(Blocks(last_block.X + last_block.W,last_block.Y,last_block.W,last_block.H,rand_color(),display))
            return next_row
    
    


