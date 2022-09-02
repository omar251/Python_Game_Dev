from turtle import delay
import pygame
from rgb import *
class Blocks:
    randx,randy = random.randint(-10, 10),random.randint(-10, 10)
    ball_speed = 5
    
    def __init__(self, x, y, w, h, color,display):
        self.B_loc = {'X': x, 'Y': y}
        self.B_size = {'width': w, 'height': h}
        self.W = w
        self.H = h
        self.top    = y
        self.right  = x+w
        self.left   = h,x
        self.bottom = y+h
        self.centerX = x - (self.W/2)
        self.centerY = y - (self.H/2)
        self.X = x
        self.Y = y
        self.color = color
        self.display = display
        self.dx = 0
        self.dy = 0 
        # print(self.top,self.right,self.left,self.bottom)

    def draw_block(self,display):
        pygame.draw.rect(display,self.color,(self.X,self.Y,self.W,self.H))
    
    def initial_block_move(self):
        self.dx,self.dy = self.randx,self.randy
    def center_block(self,x,y):
        if x==1:
            self.X = self.centerX
        if y==1:
            self.Y = self.centerY
    def move_block(self):
        self.X += self.dx
        self.Y += self.dy
    
    def get_coordinates(self):
        self.top    =  self.Y
        self.right  =  self.X+self.W
        self.left   =  self.X
        self.bottom =  self.Y+self.H
    
    def is_under(self,obj):
        self.get_coordinates()
        if( self.top > obj ):                                         
            return True
        else:
            return False      
         




        