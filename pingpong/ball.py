from blocks import Blocks
from rgb import *
class Ball(Blocks):
    def __init__(self, x, y, w, h, color,display):
        Blocks.__init__(self, x, y, w, h, color,display)
        self.lastmove = ""
        self.score = 0
        self.ball_speed = 15
   
    def bounce_border(self):
        if self.left <= 0 or self.right >= (self.display.get_width()):
            self.dx = self.dx * -1
        if self.top <= 0:# or self.Y >= (self.display.get_height()):
            self.dy = self.dy * -1
        self.draw_block()

    def start_move(self,x,y):
        self.dx,self.dy = x,y #self.randx,self.randy

    def ball_collide(self,obj):
        self.bounce_border()
        if self.is_collide(obj):
            obj.draw_block()
            self.dy *= -1
        self.bounce_border()
        
    def bounce_racket(self,racket):
        self.get_coordinates()
        racket.get_coordinates()
        self.bounce_border()           
        if (self.right >= racket.left) and (self.left <= racket.right): 
            if (self.bottom == racket.top):
                self.dy *= -1 
                if racket.is_moving:            
                    if racket.lastmove == "right":
                        self.dx = abs(self.ball_speed)
                        self.lastmove = racket.lastmove
                    elif racket.lastmove == "left": 
                        self.dx = -abs(self.ball_speed)
                        self.lastmove = racket.lastmove
                else:
                    self.dx = 0
                    self.lastmove ="stop"

                self.score += 1        

    

    
        