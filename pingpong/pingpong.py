import pygame
from blocks import *
from rgb import *

running = True
fps = 500 
dx,dy = 0,0
lastmove = ""
def draw_screen(display):
    display.fill(black)
    ball.draw_block(display)
    racket.draw_block(display)
    pygame.display.update()

pygame.init()
pygame.display.set_caption('ping pong')
dis = pygame.display.set_mode((500, 500))

ball = Blocks(250,250,25,25,rand_color(),dis)
racket = Blocks(250,490,200,10,rand_color(),dis)

ball.start_move()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    ball.bounce_ball_racket(racket)
    # ball.bounce_ball_border()
    ball.move_block()
    lastmove = racket.move_racket(lastmove)
    draw_screen(dis)