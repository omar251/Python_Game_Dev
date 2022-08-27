from pickle import TRUE
import random
import pygame
from blocks import * 
from rgb import *
from background import *

fps = 25

pygame.init()
pygame.display.set_caption('SNAKE')
dis = pygame.display.set_mode((500, 500))
a,b = random_loc(500,500)

head = Blocks(30, 30, 25, 25, green,dis)
tail = head.child(dis)
food = Blocks(a,b, 15, 15, red,dis)

dis.fill(black)

def draw_screen(display):
    display.fill(black)
    pygame.draw.rect(display, food.color, (a,b, food.W, food.H))
    pygame.draw.rect(display, head.color, (head.X, head.Y, head.W, head.H))
    pygame.draw.rect(display, white, (tail.X, tail.Y, tail.W, tail.H))
    pygame.display.update()
dx,dy = 0,0
lastmove = ""
pause = True
eaten = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    draw_screen(dis)
    write_score(dis,eaten)
    dx,dy,lastmove = head.move(dx,dy,lastmove)
    print (dx,dy)
    tail.move_child(head.X,head.Y,dx,dy)
    if(head.is_eating(food, a,b)):
        eaten += 1
        head.draw_snake(dis)
        a,b =random_loc(400,400)
    if head.is_border():
        write_stuff(dis,'YOU LOST', 24, red, 179, 230)
        eaten = 0
        

from pickle import TRUE
import random
import pygame
from blocks import * 
from rgb import *
from background import *

fps = 25

pygame.init()
pygame.display.set_caption('SNAKE')
dis = pygame.display.set_mode((500, 500))
a,b = random_loc(500,500)

head = Blocks(30, 30, 25, 25, green,dis)
tail = head.child(dis)
food = Blocks(a,b, 15, 15, red,dis)

dis.fill(black)

def draw_screen(display):
    display.fill(black)
    pygame.draw.rect(display, food.color, (a,b, food.W, food.H))
    pygame.draw.rect(display, head.color, (head.X, head.Y, head.W, head.H))
    pygame.draw.rect(display, white, (tail.X, tail.Y, tail.W, tail.H))
    pygame.display.update()
dx,dy = 0,0
lastmove = ""
pause = True
eaten = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    draw_screen(dis)
    write_score(dis,eaten)
    dx,dy,lastmove = head.move(dx,dy,lastmove)
    print (dx,dy)
    tail.move_child(head.X,head.Y,dx,dy)
    if(head.is_eating(food, a,b)):
        eaten += 1
        head.draw_snake(dis)
        a,b =random_loc(400,400)
    if head.is_border():
        write_stuff(dis,'YOU LOST', 24, red, 179, 230)
        eaten = 0
        

