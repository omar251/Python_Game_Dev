import pygame, sys, random
from pygame.locals import *
pygame.init()
pygame.display.set_caption('SNAKE')
dis = pygame.display.set_mode((500, 500))

eaten = 0
move = 10
black = (0, 0, 0)
white = (225, 225, 225)
red = (255, 0, 0)
green = (0, 225, 0)
clock = pygame.time.Clock()
FPS = 24
rand_loc = [random.randint(0, 500), random.randint(0, 500)]
d_x = 0
d_y = 0

class Blocks:
    def __init__(self, x, y, w, h, color):
        self.B_loc = {'X': x, 'Y': y}
        self.B_size = {'width': w, 'height': h}
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.WX = x + w
        self.HY = y + h
        self.color = color
        # self.B_corners = {'TL':(x, y),'TR':(x+w, y), 'BL':(x,y+h),'BR':(x+w, y+h)}
        # self.B_corners = [[x, y],  [x + w, y],  [x, y + h],  [x + w, y + h]]
        pygame.draw.rect(dis, color, (x, y, w, h))


player = Blocks(30, 30, 25, 25, green)
token = Blocks(rand_loc[0], rand_loc[1], 15, 15, red)
#tail = Blocks(5, 30, 25, 25, green)


def is_collide(self, X, Y):
    if X < player.X + player.W and X + self.W > player.X and Y < player.Y+player.H \
and self.H + Y > player.Y:
        return True


def is_border():
	if player.X == 0 or player.Y == (480) or player.X == (480) or player.Y ==0:
		return True
	else:
		return False


def draw_screen(display):
    display.fill(black)
    pygame.draw.rect(display, token.color, (rand_loc[0], rand_loc[1], token.W, token.H))
    pygame.draw.rect(display, player.color, (player.X, player.Y, player.W, player.H))
    pygame.display.update()


def write_score(display):
    myfont = pygame.font.SysFont('Comic Sans MS', 16, True)
    score = myfont.render('score '+str(eaten), False, white)
    display.blit(score, (380, 5))
    pygame.display.update()


def write_stuff(display, string, size, color, p_x, p_y):
    da_font = pygame.font.SysFont('Comic Sans MS', size, True)
    word = da_font.render(str(string), False, color)
    display.blit(word, (p_x, p_y))
    pygame.display.update()


pause = False
run = True
while run:
    # pygame.time.delay(50)
    pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.Y >= 3:
        d_x = 0
        d_y = -1
    elif keys[pygame.K_DOWN]and player.Y < (500-player.H):
        d_x = 0
        d_y = 1
    elif keys[pygame.K_RIGHT] and player.X < (500-player.W):
        d_x = 1
        d_y = 0
    elif keys[pygame.K_LEFT]and player.X >= 3:
        d_x = -1
        d_y = 0
    player.X += (move * d_x)
    player.Y += (move * d_y)
    if keys[pygame.K_SPACE]:
        d_x = 0
        d_y = 0
        pause = True
    clock.tick(FPS)
    # print(player.X, player.Y)
    draw_screen(dis)
    write_score(dis)
    if is_collide(token, rand_loc[0], rand_loc[1]):
        eaten += 1
        # add tail block to snake
        rand_loc = [random.randint(0, 400), random.randint(0, 400)]
    if is_border():
        write_stuff(dis, 'YOU LOST', 24, red, 179, 230)
        pygame.quit()
        sys.exit()

