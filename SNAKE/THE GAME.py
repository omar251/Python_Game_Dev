from pickle import TRUE
import pygame
from blocks import * 
from rgb import *
from background import *
import time

fps = 25

pygame.init()
pygame.display.set_caption('SNAKE')
dis = pygame.display.set_mode((500, 500))
a,b = random_loc(200,200)
snake = []

head = Blocks(30, 30, 10, 10, rand_color(),dis)
snake.append(head)
x=2                                                                      #making body length 3 squares
while x != 0:
    head.create_child(snake,dis)
    x-=1

food = Blocks(a,b, 30, 30, rand_color(),dis)

dis.fill(black)

def draw_screen(display):                                                #screen initialization
    display.fill(black)
    pygame.draw.rect(display, food.color, (a,b, food.W, food.H))
    for obj in snake:                                                    # loops over snake list elements to render each
        pygame.draw.rect(display,obj.color,(obj.X,obj.Y,obj.W,obj.H))
    pygame.display.update()

dx,dy = 0,0                                                              # variable initialization
lastmove = ""
pause = True
eaten = 0
running = True

while running:                                                           # main game loop
    for event in pygame.event.get():                                     #close window button feature
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)                                        #difficulty / frame rate
    draw_screen(dis)                                                     #screen update
    write_score(dis,eaten)
    dx,dy,lastmove = head.move(dx,dy,lastmove)
    size = len(snake) - 1                                                #snake array size
    i = 0                                                                 # remaining snake to be rendered
    j = 1
    while size > 0:                                                      #self = snake[i+1] & father = snake[i]
        #snake[i+1].move_child(snake[i].X,snake[i].Y)                    #produces choppy snake
        snake[i+1].move_snake(snake[i])                                  #smoother preformance 
        size -= 1                                                        # this section is to maintain snake size
        i += 1
    if(head.is_eating(food, a,b)):
        eaten += 1
        
        a,b =random_loc(200,200)
        head.create_child(snake,dis)
    if head.is_border():
        write_stuff(dis,'YOU LOST', 24, red, 179, 230)
        eaten = 0
        head.X=250
        head.Y=250
        reset(snake)
        #running = False
        
    if head.is_collide(snake,dis):
        eaten=0
        reset(snake)
        
 
