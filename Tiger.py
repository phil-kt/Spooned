import pygame
class Tiger(object):       
    def __init__(self, x, y, direction):
        self.image = pygame.image.load("tigerVomit_2.png").convert_alpha()
        self.rect = pygame.Rect(x,y,100,60)
        if direction[0] == 1:
            self.dx = 20
        elif direction[1] == 1:
            self.dx = -20
        else:
            self.dx = 15
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 100
        self.frame = 0
    def update(self, x, y, deltaTime):
        self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame + 1) % 4
            self.elapsed = 0
        self.rect.centerx += self.dx  
    def draw(self, screen):
        screen.blit(self.image, self.rect, pygame.Rect(0,0,100,60))