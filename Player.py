import pygame
class Player(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("Kevin_spriteSheet.png").convert_alpha()
        self.rect = pygame.Rect(x,y,150,150)
        self.direction = [0,0,0] #right, left, duck
        self.vel_up = 0
        self.jump = True
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 100
        self.frame = 0
        self.duck = False
        self.hit = False
    def update (self, width, height, deltaTime, obstacleRects):
        #moving right
        collide = False
        if not self.jump and not self.duck:
            self.targetRow = 0
        if (self.direction[0] == 1) and (self.direction[1] != 1) and not self.duck:
            futurerect = self.rect.move(10, 0)
            self.targetRow = 1
            if (futurerect.right) <= width: 
                #collision
                for tile in obstacleRects:
                    if futurerect.colliderect(tile):
                        collide = True
                if not collide:
                    self.rect = futurerect
        #moving left
        if (self.direction[1] == 1) and (self.direction[0] != 1) and not self.duck:
            futurerect = self.rect.move(-10, 0)
            self.targetRow = 2
            if (futurerect.left) >= 0:
                #collision
                for tile in obstacleRects:
                    if futurerect.colliderect(tile):
                        collide = True
                if not collide:
                    self.rect = futurerect
        #ducking
        
        #gravity
        if self.rect.bottom <= 720:
            if self.jump == True:
                self.vel_up +=2
            futurerect = self.rect.move(0, self.vel_up)
            if futurerect.top >= 0 and futurerect.bottom < 720:
                for tile in obstacleRects:    
                    if futurerect.colliderect(tile):
                        collide = True
                        self.rect.bottom = tile.top
                        self.jump = False
                if not collide:
                    self.rect = futurerect
            if futurerect.bottom > 720 and not collide:
                self.jump = False
                self.rect.bottom = height
                collide = True
        if not self.jump:
            self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame +1) % 8
            self.elapsed = 0
    def draw(self, screen):
        if self.jump and self.vel_up == 0:
            self.frame = 1
        if self.duck and not self.jump and self.direction[0] != 1 and self.direction[1] != 1:
            screen.blit(self.image,self.rect, pygame.Rect(self.frame*150,self.targetRow*150+90,150,90))
        else:
            screen.blit(self.image, self.rect, pygame.Rect(self.frame*150, self.targetRow*150, 150, 150))