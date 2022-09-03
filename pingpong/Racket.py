import pygame
from blocks import Blocks
from rgb import *
class Racket(Blocks):
    Racket_speed = 10
    def __init__(self, x, y, w, h, color,display):
        super().__init__(x, y, w, h, color,display)
        self.lastmove=""
        self.is_moving = False

    def move_racket(self):
        keys = pygame.key.get_pressed()
        keypressed=False
        if keys[pygame.K_RIGHT] and (self.lastmove !="right"):
            self.dx =  self.Racket_speed
            self.lastmove  = "right"
            keypressed= True
            self.is_moving = True
        elif keys[pygame.K_LEFT] and (self.lastmove !="left"):
            self.dx =  self.Racket_speed * -1
            self.lastmove  = "left"
            keypressed= True
            self.is_moving = True
        elif self.left <= 0 or (self.right) >= (self.display.get_width()):
            self.dx = 0
            keypressed=False
            self.is_moving = False
        self.move_block()
        self.draw_block()
        return keypressed