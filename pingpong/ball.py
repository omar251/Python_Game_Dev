from blocks import Blocks
from rgb import *
class Ball(Blocks):
    def __init__(self, x, y, w, h, color,display):
        Blocks.__init__(self, x, y, w, h, color,display)
        self.score = 0
   
    def bounce_racket(self,racket):
        self.get_coordinates()
        racket.get_coordinates()
        if self.left <= 0 or self.right >= (self.display.get_width()) :
            self.dx = self.dx * -1
        if (self.top <= 0):
            self.dy = self.dy * -1           
        if (self.right >= racket.left) and (self.left <= racket.right): 
            if (self.bottom == racket.top):
                self.dy *= -1
                self.score += 1

    def bounce_border(self):
        if self.X <= 0 or self.X >= (self.display.get_width()):
            self.dx = self.dx * -1
        if self.Y <= 0 or self.Y >= (self.display.get_height()):
            self.dy = self.dy * -1

        