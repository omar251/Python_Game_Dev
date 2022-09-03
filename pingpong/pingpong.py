from turtle import width
import pygame
from Racket import *
from background import *
from blocks import *
from rgb import *
from ball import *

running = True 
fps = 60
width,height = 500,500
pygame.init()
pygame.display.set_caption('ping pong')
dis = pygame.display.set_mode((width, height))
bricks = []
next_row = 0
bricks.append(Blocks(20,100,20,20,rand_color(),dis))
brick_size = 250
while brick_size > 0:
    next_row = create_bricks(dis,bricks,next_row)
    brick_size -=1
ball = Ball(width/2,height/2,20,20,rand_color(),dis)
racket = Racket(width/2,height-30,250,10,rand_color(),dis)
racket.center_block(1,0)
restart = True
# ball.start_move() 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    dis.fill(black)
    ball.bounce_racket(racket)
    if(ball.is_under(dis.get_height())):
        restart = True
    
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

    for bar in bricks:
        ball.ball_collide(bar)
        bar.draw_block()
        if ball.is_collide(bar):
            bricks.remove(bar)
    pygame.display.update()
    
    write_score(dis,ball.score)
    print(ball.lastmove,"+++",racket.lastmove,racket.is_moving)
    