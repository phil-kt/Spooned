import pygame, sys, Enemy, Player, Spoon, Table, Health, levelEdit, menu   
from Player import *
from Table import *
from Spoon import *
from Enemy import *
from Health import *
from levelEdit import *
from Tiger import *
from TigerWoods import *
from E_Spoon import *
from E_Spoon2 import *
from menu import *
from Dancer import *

pygame.init()
screen = pygame.display.set_mode((1200, 720))
background = pygame.Surface((14400, 720))
pygame.mixer.music.load("background_Loop_long.ogg")
pygame.mixer.music.play(-1)
#scroll through screen
vpRenderOffset = (0,0)
vpStatsOffset = (80,540)
vpCoordinate = 0
minHorzScrollBounds = 0
maxHorzScrollBounds = 14400  # 1996 = 2636 - 640
advanceVelocity = 0
scrollVelocity = 10
# generate an event 30 times a second, and perform simulation update. this
# keeps the game running at the same speed in framerate-independent fashion.
# map stuff
UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, int(1000.0/30))
obstacles, obstacleRects, aiRects = load_map() 
# declaring variables
clock = pygame.time.Clock()
dancer = Dancer(0, 20)
player = Player(200,200)
enemy_list = [Enemy(800,350), Enemy(1500,450), Enemy(2400,350), Enemy(3350,350), \
              Enemy(4000, 450), Enemy(4600, 350),Enemy(5300, 450), Enemy(5600, 350), \
              Enemy(6000, 350), Enemy(6600, 450), Enemy(7800, 350), Enemy(8700,450), \
              Enemy(9600,450), Enemy(11400,450), Enemy(11800,450), Enemy(12450,350)]
tigerwoods = TigerWoods(15500,300)
healthBar = Health(20, 20)
health = 12
playing = True
# player shots/damage
shots = []
fired = False
cooldown = 1000
firetime = 0
i_timer = 0
# enemy shots
shots_e = []
fired_e = False
cooldown_e = 1000
firetime_e = 0
dt = 16
# tiger shots
shots_t = []
cooldown_t = 1000
firetime_t = 0
tigerwoods.move()
#win/lose
lose = False
win = False
horse = pygame.image.load("victory.png")
horse2 = pygame.image.load("victory2.png")
phil = pygame.image.load("gameOver1.png")
phil2 = pygame.image.load("gameOver2.png")

for enemy in enemy_list:
    enemy.move()

menu()
    
while playing:
    time = pygame.time.get_ticks()
    clock.tick(30)
# input phase
    
    # moving the player around screen and shooting
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                player.direction[0] = 1
            elif (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                player.direction[1] = 1
            elif (event.key == pygame.K_s) or (event.key == pygame.K_DOWN) and not player.jump and player.direction[0] != 1 and player.direction[1] != 1:
                player.rect = pygame.Rect(player.rect.left,player.rect.top,60,60)
                player.targetRow = 4
                player.frame = 0
                player.duck = True
            if player.jump == False:    
                # jumping
                if (event.key == pygame.K_w) or (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP):
                    player.vel_up = -25
                    player.jump = True
                    player.targetRow = 3
                    player.frame = 0
            if len(shots) < 3:
                if event.key == pygame.K_g and not fired:
                    shots.append(Spoon(player.rect.centerx, player.rect.midtop[1]+30, player.direction))
                    fired = True
                    firetime = pygame.time.get_ticks()
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_d) or (event.key == pygame.K_RIGHT):
                player.direction[0] = 0
                if not advanceVelocity == 0:
                    advanceVelocity += -scrollVelocity
            elif (event.key == pygame.K_a) or (event.key == pygame.K_LEFT):
                player.direction[1] = 0
            elif (event.key == pygame.K_s) or (event.key == pygame.K_DOWN) and not player.jump and player.direction[0] != 1 and player.direction[1] != 1:
                player.rect = pygame.Rect(player.rect.left,player.rect.top-75,150,150)
                player.duck = False
        elif event.type == UPDATE:
            vpCoordinate += advanceVelocity
            if vpCoordinate < minHorzScrollBounds:
                vpCoordinate = minHorzScrollBounds
            if vpCoordinate > maxHorzScrollBounds:
                vpCoordinate = maxHorzScrollBounds
                
    # enemy shooting 
    for enemy in enemy_list:
        enemy.shoot = random.randint(0,10)	
    for enemy in enemy_list:
        if len(shots_e) < 3:
            if enemy.shoot == 5 and enemy.rect.left < vpCoordinate + 1200 and enemy.rect.right > vpCoordinate:
                spoon_type = random.randint(0,1)
                if spoon_type == 0: 
                    shots_e.append(E_Spoon(enemy.rect.centerx, enemy.rect.midtop[1]+30, enemy.direction))
                elif spoon_type == 1:
                    shots_e.append(E_Spoon2(enemy.rect.centerx, enemy.rect.midtop[1]+30, enemy.direction))
                fired_e = True
                firetime_e = pygame.time.get_ticks()
                
    # tiger shooting
    tigerwoods.shoot = random.randint(0,10)
    if tigerwoods.seek == False and tigerwoods.attack == False:
        if len(shots_t) < 2:
            # print tigerwoods.rect.midtop[1]
            if tigerwoods.shoot == 10:
                shots_t.append(Tiger(tigerwoods.rect.centerx, tigerwoods.rect.centery - 40, tigerwoods.direction))
                tigerwoods.firing = True
                firetime_t = pygame.time.get_ticks()
 
    # cooldown
    if firetime + cooldown < pygame.time.get_ticks():
        fired = False 
    if firetime_e + cooldown_e < pygame.time.get_ticks():
        fired = False                
        
# update phase
    if player.direction[0] == 1 and player.rect.right > 600:
        if (player.rect.right) < 14400:
            advanceVelocity = scrollVelocity
        if (vpCoordinate) >= 13200:
            advanceVelocity = 0
    player.update(14400, 720, dt, obstacleRects) 
    for enemy in enemy_list:
        enemy.update(vpCoordinate, vpCoordinate + 1200, dt, aiRects) 
    tigerwoods.update(vpCoordinate,vpCoordinate + 1200, dt, player, aiRects)
    
    # drawing player shots
    for x in shots:
        col = False
        x.update(player.rect.right, player.rect.centery, dt)
        if x.rect.left > vpCoordinate + 1200 or x.rect.right < vpCoordinate:
            shots.remove(x)
            continue
        if x.rect.colliderect(tigerwoods.rect):
            shots.remove(x)
            tigerwoods.hp -= 1
            if tigerwoods.hp <= 0:
                playing = False
                win = True
            continue
        for tile in obstacleRects:
            if x.rect.colliderect(tile):
                shots.remove(x)
                col = True
                break
        if col: continue
        for enemy in enemy_list:
            if x.rect.colliderect(enemy):
                shots.remove(x)
                enemy_list.remove(enemy)
                col = True
                break
        if col: continue
        
    # drawing enemy shots
    for x in shots_e:
        col = False
        x.update(enemy.rect.right, enemy.rect.centery,dt)
        if x.rect.left > vpCoordinate + 1200 or x.rect.right < vpCoordinate:
            shots_e.remove(x)
            continue
        for tile in obstacleRects:
            if x.rect.colliderect(tile):
                shots_e.remove(x)
                col = True
                break
        if col: continue
        # losing health
        if x.rect.colliderect(player.rect):
            health -= 1
            shots_e.remove(x) 
            i_timer = pygame.time.get_ticks()
            if health >= 0:
                healthBar.image = pygame.image.load("health%d.png"%(health))
            if health < 0:
                health = 0
            col = True
            break

    # drawing tiger's shots
    for x in shots_t:
        col = False
        x.update(tigerwoods.rect.right, tigerwoods.rect.centery,dt)
        if x.rect.left > vpCoordinate + 1200 or x.rect.right < vpCoordinate:
            shots_t.remove(x)
            col = True
            continue
        if col: continue
        if x.rect.colliderect(player.rect):
            health -= 2
            shots_t.remove(x)
            if health >= 0:
                healthBar.image = pygame.image.load("health%d.png"%(health))
            if health < 0:
                health = 0
                playing = False
                lose = True
            col = True
            break
        
    # collide with enemy
    for enemy in enemy_list:
        if player.hit == False:
            if player.rect.colliderect(enemy):
                i_timer = pygame.time.get_ticks()
                player.hit = True
                health -= 1
                if health >= 0:
                    healthBar.image = pygame.image.load("health%d.png"%(health))
                if health < 0:
                    health = 0
                    playing = False 
                    lose = True
    if player.hit == False:
        if tigerwoods.rect.colliderect(player.rect):
            i_timer = pygame.time.get_ticks()
            player.hit = True
            health -=3
            if health >= 0:
                healthBar.image = pygame.image.load("health%d.png"%(health))
            if health < 0:
                health = 0
                playing = False 
                lose = True
    if i_timer + 2000 < pygame.time.get_ticks():
        player.hit = False
# draw phase
    screen.fill((0,0,0))
    background.blit(obstacles, obstacles.get_rect())
    player.draw(background)
    for enemy in enemy_list:
        enemy.draw(background)
    if tigerwoods.firing == True:
        tigerwoods.vomit(background)
    else:
        tigerwoods.draw(background)
    for x in shots:
        x.draw(background)
    for x in shots_e:
        x.draw(background)
    for x in shots_t:
        x.draw(background)
    vpCoordinate = min([vpCoordinate,player.rect.left - 100])
    viewport = background.subsurface((vpCoordinate, 0) + (1200, 720))
    screen.blit(viewport, vpRenderOffset)
    healthBar.draw(screen)
    pygame.display.flip()
    dt = pygame.time.get_ticks()-time
    
currentTime = pygame.time.get_ticks()
currentHorse = horse
currentPhil = phil
elapsed = 0 
 
# losing
while lose == True:
    elapsed += pygame.time.get_ticks() - currentTime
    screen.blit(currentPhil, pygame.Rect(0,0,1200,720))
    if elapsed > 3000:
        currentTime = pygame.time.get_ticks()
        elapsed = 0
        if currentPhil == phil:
            currentPhil = phil2
        else: currentPhil = phil
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

# winning /CharlieSheen
while win == True:
    elapsed += pygame.time.get_ticks() - currentTime
    screen.blit(currentHorse, pygame.Rect(0,0,1200,720))
    if elapsed > 1000:
        currentTime = pygame.time.get_ticks()
        elapsed = 0
        if currentHorse == horse:
            currentHorse = horse2
        else: currentHorse = horse
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
