import pygame
from rgb import *
class Blocks:
    
    def __init__(self, x, y, w, h, color,display):
        self.B_loc = {'X': x, 'Y': y}
        self.B_size = {'width': w, 'height': h}
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.WX = x + w
        self.HY = y + h
        self.color = color
        self.display = display
        # pygame.draw.rect(canvas, color, (x, y, w, h))
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

        return dx,dy,keypressed
    def move_child(self,x,y):
        # self.X = x - dx*2
        # self.Y = y - dy*2

        xx = x - self.X
        yy = y - self.Y
        if xx > 25:
            self.X = self.X + 25
            self.Y = y
        elif xx < -25:
            self.X = self.X - 25
            self.Y = y
        elif yy > 25:
            self.Y = self.Y + 25
            self.X = x
        elif yy < -25:
            self.Y = self.Y - 25
            self.X = x
        # self.X = self.X + dx
        # self.Y = self.Y + yy
        print("  ")

         
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
        # snake.append(child)
        return child
    def create_child(self,snake,display):
        father = snake[len(snake)-1]
        snake.append(Blocks(father.X-father.W,father.Y,father.W,father.H,father.color,display))
        return snake
    def draw_snake(self,display):
        display.fill(black)
        pygame.draw.rect(display, red, (self.X, self.Y, self.W, self.H))
        pygame.display.update()