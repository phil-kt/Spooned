import pygame
class Dancer(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("spriteSheet.png").convert_alpha()
        self.rect = pygame.Rect(x,y,600,600)
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 100
        self.frame = 0
    def update (self, deltaTime):
        print self.frame, self.targetRow        
        self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame +1 ) % 5
            self.elapsed = 0
            if self.frame == 4:
                self.targetRow += 1
                self.frame = 0
            if self.targetRow == 4 and self.frame == 2:
                # print 'condition met'
                self.frame = 0
                self.targetRow = 0
    def draw(self, screen):    
        screen.blit(self.image, self.rect, pygame.Rect(self.frame*600, self.targetRow*600, 600, 600))