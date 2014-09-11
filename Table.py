import pygame
class Table(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("table.png").convert_alpha()
        self.rect = pygame.Rect(x,y,150,80)
    def draw(self, screen):
        screen.blit(self.image, self.rect)