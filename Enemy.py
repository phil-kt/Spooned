import pygame, random
class Enemy(object):
    def __init__(self, x, y):
        self.image = pygame.image.load("ian.png").convert_alpha()
        self.rect = pygame.Rect(x,y,150,150)
        self.vel_x = 2
        self.direction = [0,0]
        self.shoot = 0
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 250
        self.frame = 0
	
    def update(self, minwidth, maxwidth, deltaTime, aiRects):
        if self.rect.right < minwidth or self.rect.left > maxwidth:
            return
        bounce = False
		#This section keeps enemy on screen	
        if self.direction[0] == 1 and self.direction[1] != 1:
            self.targetRow = 1
            futurerect = self.rect.move(self.vel_x, 0)
            for tile in aiRects:
                if futurerect.colliderect(tile):
                    bounce = True
                    self.direction[0] = 0
                    self.direction[1] = 1
            if not bounce:
                self.rect = futurerect
		
        if self.direction[1] == 1 and self.direction[0] != 1:
            self.targetRow = 0
            futurerect = self.rect.move(-self.vel_x, 0)
            for tile in aiRects:
                if futurerect.colliderect(tile):
                    bounce = True
                    self.direction[0] = 1
                    self.direction[1] = 0
            if not bounce:
                self.rect = futurerect
        self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame +1) % 4
            self.elapsed = 0
    def move(self):
        self.direction[0] = random.choice([0,1])
        self.direction[1] = not self.direction[0]
        #sets the enemy either going left or right
	
    def draw(self, screen):
        screen.blit(self.image, self.rect, pygame.Rect(self.frame*150, self.targetRow*150, 150, 150))
	