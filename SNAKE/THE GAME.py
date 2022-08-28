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
snake = []

head = Blocks(30, 30, 25, 25, white,dis)
snake.append(head)
# snake.append(head)
# head.create_child(snake,dis)
# head.create_child(snake,dis)
x=2
while x != 0:
    create_child(snake,dis)
    x-=1
# tail = head.child(dis)
# tail2 = tail.child(dis)

food = Blocks(a,b, 15, 15, red,dis)

dis.fill(black)

def draw_screen(display):
    display.fill(black)
    pygame.draw.rect(display, food.color, (a,b, food.W, food.H))
    for obj in snake:
        pygame.draw.rect(display,green,(obj.X,obj.Y,obj.W,obj.H))
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
    # tail.move_child(head.X,head.Y)
    # tail2.move_child(tail.X,tail.Y)
    size = len(snake) - 1
    i = 1
    while size > 0:
        snake[i].move_child(snake[i-1].X,snake[i-1].Y)
        size -= 1
        i += 1
        print(i)
    if(head.is_eating(food, a,b)):
        eaten += 1
        # head.draw_snake(dis)
        a,b =random_loc(400,400)
        create_child(snake,dis)
    if head.is_border():
        write_stuff(dis,'YOU LOST', 24, red, 179, 230)
        eaten = 0
        