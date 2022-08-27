import pygame
from rgb import *
class Blocks:
    
    def __init__(self, x, y, w, h, color,canvas):
        self.B_loc = {'X': x, 'Y': y}
        self.B_size = {'width': w, 'height': h}
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.WX = x + w
        self.HY = y + h
        self.color = color
        pygame.draw.rect(canvas, color, (x, y, w, h))
    def move(self,dx,dy,last):
        keys = pygame.key.get_pressed()
        keypressed = last
        if keys[pygame.K_UP] and self.Y >= 3 and keypressed !="down":
            dx =  0
            dy =  -10
            keypressed = "up"
        elif keys[pygame.K_DOWN]and self.Y < (500-self.H) and keypressed !="up":
            dx =  0
            dy =  10
            keypressed = "down"
        elif keys[pygame.K_RIGHT] and self.X < (500-self.W) and keypressed !="left":
            dx =  10
            dy =  0
            keypressed = "right"
        elif keys[pygame.K_LEFT]and self.X >= 3 and keypressed !="right":
            dx =  -10
            dy =  0
            keypressed = "left"
        if keys[pygame.K_SPACE]:
            dx = 0
            dy = 0
            keypressed = "space"
            pause = True
        self.X += dx
        self.Y += dy
        print(keypressed)
        return dx,dy,keypressed
    def move_child(self,x,y,dx,dy):
        if dx < 0:
            self.X = x + self.H
        elif dx >= 0:
            self.X = x - self.H
            
        if dy < 0:
            self.Y = y + self.W
        elif dy >= 0:
            self.Y = y - self.W
         
    def is_eating(self,target, X, Y):
        if X < self.X + self.W and X + target.W > self.X and Y < self.Y+self.H \
and target.H + Y > self.Y: 
            return True
    
    def is_border(self):
        if self.X == 0 or self.Y == (480) or self.X == (480) or self.Y ==0:
            return True
        else:
            return False
    def child(self,display):
        child = Blocks(self.X-self.W, self.Y, self.W, self.H, self.color,display)
        pygame.draw.rect(display, child.color, (child.X, child.Y, child.W, child.H))
        pygame.display.update()
        return child

    def draw_snake(self,display):
        display.fill(black)
        pygame.draw.rect(display, red, (self.X, self.Y, self.W, self.H))
        pygame.display.update()