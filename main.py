import pygame

import random

pygame.init()


#fenster
WIDTH = 1080
HEIGHT = 720
RESOLUTION = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(RESOLUTION)

#player
floor_width, floor_height = 1080, 20
player_WIDHT, player_HEIGHT = 20, 20
pos_x, pos_y = (WIDTH-player_WIDHT)//2, (HEIGHT-player_HEIGHT-floor_height)
player = pygame.Rect(pos_x, pos_y, player_HEIGHT, player_WIDHT)
PLAYER_SPEED = 6

#balken
is_running = True
pos_barx, pos_bary = 0 , 0
bar_width, bar2_width = WIDTH//2, 350
pos_barx2, pos_bary2 = WIDTH - bar2_width , 0
bar = pygame.Rect(pos_barx, pos_bary, bar_width, 50)
bar2 = pygame.Rect(pos_barx2, pos_bary2, bar2_width, 50)

#floor
pos_a, pos_b = 0, 700
floor = pygame.Rect(pos_a, pos_b, floor_width, floor_height)
#uhr
CLOCK = pygame.time.Clock()
FPS = 60

#gameloop
while is_running == True:
    screen.fill('blue')

#eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
#bewegung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == True:
        player.left = player.left - PLAYER_SPEED
    elif keys[pygame.K_RIGHT] == True:
        player.right = player.right + PLAYER_SPEED
#balken down
    down = 7.5
    if is_running:
        bar.y += down
        bar2.y += down
#collide
    if player.colliderect(bar):
        is_running = False
    if player.colliderect(bar2):
        is_running = False

#loch in bar
    if bar.y >= HEIGHT:
        bar.y = 0
        bar2.y = 0
        HOLE_WIDTH = 200
        hole_x = random.randint(100, WIDTH - 100 - HOLE_WIDTH)
        bar.width = hole_x
        bar2.width = WIDTH - (hole_x + HOLE_WIDTH)
        bar2.x = hole_x + HOLE_WIDTH
#score
    score = 0
    if bar.y and bar2.y == player_HEIGHT:
        score += 1
    if player.colliderect(bar and bar2):    
        print(score)
    
#dmdmmdmdmdmdmdmmdmdm

    #zeichnen
    pygame.draw.rect(screen, 'white', player)
    pygame.draw.rect(screen, 'green', floor)
    pygame.draw.rect(screen, 'black', bar)
    pygame.draw.rect(screen, 'black', bar2)
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()