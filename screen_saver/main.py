import pygame
from blocks import *
from rgb import *
from background import *
from PIL import Image
fps = 5000
row = []
# im = Image.open(r"C:\Users\PC\OneDrive - Arab Academy for Science and Technology\Desktop\pixel_image433_500.png")
# pix_val = list(im.getdata())
pygame.init()
pygame.display.set_caption('test')
dis = pygame.display.set_mode((500, 500))
# def draw_image(display,pixels):
#     for j in range(0,500):
#         for i in range(0,433):
#             pygame.draw.rect(display,pixels[433*j+i],(i,j,1,1))
#     pygame.display.update()

# first_block = Blocks(0,0,10,10,rand_color(),dis)
x=y = 20
row.append(Blocks(0,0,x,y,rand_color(),dis))
next_row = 0
# while next_row <= 9:
#     next_row = create_row(dis,row,next_row)
#     print(next_row)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    next_row = create_row(dis,row,next_row)  
    # draw_image(dis,pix_val)
    draw_screen(dis,row)
    # for j in range(0,500):
    #     for i in range(0,200):
    #         pygame.draw.rect(dis,pix_val[433*j+i],(i,j,1,1))
    # pygame.display.update()
