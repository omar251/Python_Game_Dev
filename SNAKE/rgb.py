import random
import time
from turtle import delay
black = (0, 0, 0)
white = (225, 225, 225)
red = (255, 0, 0)
green = (0, 225, 0)
blue = (0, 0,225)
color =[blue,white,red,green,black]
def rand_color():
    rand_color = (random.randint(0, 225),random.randint(0, 225),random.randint(0, 225))
    return rand_color

