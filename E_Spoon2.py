import pygame, random
class E_Spoon2(object):       
    def __init__(self, x, y, direction):
        self.image = pygame.image.load("spoonSprites.png").convert_alpha()
        self.rect = pygame.Rect(x,y,50,50)
        if direction[0] == 1:
            self.dx = 15
        elif direction[1] == 1:
            self.dx = -15
        else:
            self.dx = 15
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 100
        self.frame = 0
    def update(self, x, y, deltaTime):
        self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame + 1) % 7
            self.elapsed = 0
        self.rect.centerx += self.dx  
    def draw(self, screen):
        screen.blit(self.image, self.rect, pygame.Rect(self.frame*50,100,50,50))