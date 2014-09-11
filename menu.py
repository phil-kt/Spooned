import pygame
from Dancer import *

def menu():
    exitMenu = False
    dancer = Dancer(-40, 20)
    dt = 16
    clock = pygame.time.Clock()
    while not exitMenu:
        time = pygame.time.get_ticks()
        clock.tick(30) 
        dancer.update(dt)
        screen = pygame.display.set_mode((1200, 720))
        screen.fill((0,0,0))
        text = pygame.font.Font(None,32)
        title = pygame.image.load("spoons.png").convert_alpha()
        prompt = text.render("Press SPACE to Start!", 1, (250,0,250))
        textClick = prompt.get_rect()
        textClick.move_ip(460,650)
        screen.blit(title, (180,-100,787,499))
        screen.blit(prompt,textClick)
        dancer.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exitMenu = True
        pygame.display.update()
        dt = pygame.time.get_ticks()-time