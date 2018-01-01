import pygame, sys
from pygame.locals import *

#Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

#Set up the window.
windowSurface = pygame.display.set_mode((500,400),0, 32) #last param, depth = 32
pygame.display.set_caption("Hello World!")

#Set up the colors.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)

#Set up the text.
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the white background onto the surface
windowSurface.fill(WHITE)

#Draw a green polygon onto the surface.
# pygame.draw.polygon(windowSurface, GREEN, ((146,0),   (291, 106),
#                                            (236,277), (56, 277),   (0, 106)  
#                                            ))

#Draw some blue lines onto the surface
# pygame.draw.line(windowSurface, BLUE, (60,60), (120, 60), 4)
# pygame.draw.line(windowSurface, BLUE, (120,60), (60, 120))
# pygame.draw.line(windowSurface, BLUE, (60,120), (120, 120), 4)

# Draw a blue circle onto the surface.
# pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw a red ellipse onto the surface
# pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#Draw the text's background rectangle onto the surface.
pygame.draw.rect(windowSurface, RED, (0,0, 10, 10))

# #Get a pixel array of the surface.
# pixArray = pygame.PixelArray(windowSurface)
# pixArray[480][380] = BLACK
# del pixArray


#Draw the text onto the surface.
# windowSurface.blit(text, textRect)

#Draw the window onto the screen.


#trail
point0 =      (0,0)
point1 =      (50, 0)
point2 =      (50, 50)
point3 =      (0, 50)
point4 =      (0, 100)
point5 =      (50, 100)
point6 =      (50, 150)
point7 =      (100, 150)
point8 =      (100, 100)
point9 =      (80, 100)
point10 =     (80, 80)
point11 =     (100, 120)
point_final = (100,0)

trail = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point_final]
trail_direction = ['r', 'd', 'l', 'd', 'r', 'd', 'r', 'u', 'l', 'u', 'r', 'u']

DOWNRIGHT = 0

enemy = {'rect': pygame.Rect(0, 0, 30, 20),
      'color': GREEN,
      'dir': DOWNRIGHT,
      'trail_point': 0
      }

tower_list = []



MOVE_SPEED = 1

def update_enemy_path(enemy):
    
    trail_point = enemy['trail_point']

    if trail_point >= len(trail):
        return
    
    destination = trail[trail_point]
    destination_x = destination[0]
    destination_y = destination[1]

    enemy_direction = trail_direction[trail_point]

    enemy_pos_x = enemy['rect'].left
    enemy_pos_y = enemy['rect'].top


    if enemy_direction == 'l':
        if enemy_pos_x <= destination_x:
            enemy['trail_point'] +=1
    elif enemy_direction == 'd':
        if enemy_pos_y >= destination_y:
            enemy['trail_point'] +=1
    elif enemy_direction == 'r':
        if enemy_pos_x >= destination_x:
            enemy['trail_point'] +=1
    elif enemy_direction == 'u':
        if enemy_pos_y <= destination_y:
            enemy['trail_point'] +=1


def update_enemy_position(enemy):
    trail_point = enemy['trail_point']
    
    if trail_point >= len(trail_direction):
        return
    
    enemy_direction = trail_direction[trail_point]
    
    if enemy_direction == 'l':
        enemy['rect'].left -= MOVE_SPEED
    elif enemy_direction == 'd':
        enemy['rect'].bottom += MOVE_SPEED
    elif enemy_direction == 'r':
        enemy['rect'].right += MOVE_SPEED
    elif enemy_direction == 'u':
        enemy['rect'].top -= MOVE_SPEED

def update_enemy(enemy):
    update_enemy_path(enemy)
    update_enemy_position(enemy)

#Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == MOUSEBUTTONUP:
        #     foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
    update_enemy(enemy)
    windowSurface.fill(WHITE)
    pygame.draw.rect(windowSurface, RED, enemy['rect'])
    pygame.display.update()
    mainClock.tick(40)