import pygame
class Health(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("health12.png")
        self.rect = pygame.Rect(x,y, 450, 85)
    def draw(self, screen):
        screen.blit(self.image, self.rect)