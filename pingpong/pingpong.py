from turtle import width
import pygame
from Racket import *
from background import *
from blocks import *
from rgb import *
from ball import *

running = True 
fps = 100 
width,height = 500,500
# def draw_screen(display):
#     display.fill(black)
#     ball.draw_block(display)
#     racket.draw_block(display)
#     pygame.display.update()

pygame.init()
pygame.display.set_caption('ping pong')
dis = pygame.display.set_mode((width, height))


ball = Ball(width/2,height/2,20,20,rand_color(),dis)
racket = Racket(width/2,height-30,width/3,10,rand_color(),dis)
racket.center_block(1,0)
restart = True

# ball.start_move() 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    if(ball.is_under(dis.get_height())):
        restart = True
    ball.bounce_racket(racket)
    if restart:
        ball.dx,ball.dy=0,0
        ball.center_block(1,1)
        if racket.move_racket():
            reset(ball)
            write_score(dis,ball.score)
            restart = False
    else:
        ball.move_block()    
        racket.move_racket()
    
    dis.fill(black)
    ball.draw_block(dis)
    racket.draw_block(dis)
    pygame.display.update()
    
    write_score(dis,ball.score)    

    