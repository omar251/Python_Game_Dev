from turtle import delay
import pygame
from rgb import *
STEP=11
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
        self.OldX = x
        self.OldY = y
        # pygame.draw.rect(canvas, color, (x, y, w, h))
    def move(self,dx,dy,last):                                      # motion originates from bottom right of screen
        keys = pygame.key.get_pressed()
        keypressed = last
        if keys[pygame.K_UP] and self.Y >= 3 and keypressed !="down":
            dx =  0
            dy =  -STEP
            keypressed = "up"
        elif keys[pygame.K_DOWN]and self.Y < (500-self.H) and keypressed !="up":
            dx =  0
            dy =  STEP
            keypressed = "down"
        elif keys[pygame.K_RIGHT] and self.X < (500-self.W) and keypressed !="left":
            dx =  STEP
            dy =  0
            keypressed = "right"
        elif keys[pygame.K_LEFT]and self.X >= 3 and keypressed !="right":
            dx =  -STEP
            dy =  0
            keypressed = "left"
        if keys[pygame.K_SPACE]:
            dx = 0
            dy = 0
            keypressed = "space"
            pause = True
        self.OldX = self.X
        self.OldY = self.Y
        self.X += dx
        self.Y += dy

        return dx,dy,keypressed
    def move_snake(self,father):      #feedback loop fills the gaps out of IF ranges (no need to move by 25)
        self.OldX = self.X
        self.OldY = self.Y
        self.X = father.OldX
        self.Y = father.OldY
        
         
    def is_eating(self,target, X, Y):
        if X < self.X + self.W and X + target.W > self.X and Y < self.Y+self.H \
and target.H + Y > self.Y: 
            return True
    
    def is_border(self):
        if 0 <= self.X <= (480) and 0 <= self.Y <= (480):
            return False
        else:
            return True

    def is_collide(self,snake,display):
        collide=None
        i=1
        size = len(snake)-1
        while size>0:
            
            if pygame.Rect.colliderect(pygame.draw.rect(display,snake[0].color,(snake[0].X,snake[0].Y,snake[0].W,snake[0].H)),pygame.draw.rect(display,snake[i].color,(snake[i].X,snake[i].Y,snake[i].W,snake[i].H))) :
                return True
            size-=1
            i+=1    
 
   
    def create_child(self,snake,display):                                                  # [USED] prioratizes the background method varient 
        father = snake[len(snake)-1]
        snake.append(Blocks(father.OldX,father.OldY,father.W,father.H,rand_color(),display))
        return snake

    def draw_snake(self,display):
        display.fill(black)
        pygame.draw.rect(display, red, (self.X, self.Y, self.W, self.H))
        pygame.display.update()