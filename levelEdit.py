#the Background is 7200 pixels by 720 pixels
#the Screen is 1200 by 720

import pygame


def load_map():
    #map tiles
    g = pygame.image.load("empty3.png").convert_alpha()
    a = pygame.image.load("empty.png").convert_alpha()
    c = pygame.image.load("cups.png").convert_alpha()
    s = pygame.image.load("empty4.png").convert_alpha()
    m = pygame.image.load("monster.png").convert_alpha()
    t1 = pygame.image.load("table-1.png").convert_alpha()
    t2 = pygame.image.load("table-2.png").convert_alpha()
    t3 = pygame.image.load("table-3.png").convert_alpha()
    t4 = pygame.image.load("table-4.png").convert_alpha()
    t5 = pygame.image.load("table-5.png").convert_alpha()
    t6 = pygame.image.load("table-6.png").convert_alpha()
    t7 = pygame.image.load("table-7.png").convert_alpha()
    t8 = pygame.image.load("table-8.png").convert_alpha()


    #reading map
    map = open("mapField.txt")

    #variables
    across = 0
    down = 0
    playerObstacleRects = []
    aiObstacleRects = []

    field =  pygame.Surface((14400, 720))
    background = pygame.image.load('cafeteriaBackground_LoopLONG.png').convert()
    field.blit(background,background.get_rect())


    #reading lines
    for line in map.readlines(): #Read # of lines
        across = 0
        for x in range(len(line)): #take variable of line
            line[x]
            if line[x] == 'g': #ground
                field.blit(g, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x] == 'a': #air
                field.blit(a, pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== 'c': #cups
                field.blit(c, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '1': #table
                field.blit(t1, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '2': #table
                field.blit(t2, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '3': #table
                field.blit(t3, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '4': #table
                field.blit(t4, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '5': #table
                field.blit(t5, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '6': #table
                field.blit(t6, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '7': #table
                field.blit(t7, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== '8': #table
                field.blit(t8, pygame.Rect(across,down,50,50))
                playerObstacleRects.append(pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== 's': #stop AI air
                field.blit(a, pygame.Rect(across,down,50,50))
                aiObstacleRects.append(pygame.Rect(across,down,50,50))
                across += 50
            elif line[x]== 'm': #general area of monsters
                field.blit(a, pygame.Rect(across,down,50,50))
                across += 50  
        down +=50
    return (field, playerObstacleRects, aiObstacleRects)
    
