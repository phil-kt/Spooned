import pygame, math, random

class TigerWoods(object):
    def __init__(self,x,y):
        self.image = pygame.image.load("tigerwoods.png").convert_alpha()
        self.attack_image = pygame.image.load("attackAnimation_Shin_Club.png").convert_alpha()
        self.vomit_image = pygame.image.load("attackAnimation_Vomit_Woods.png").convert_alpha()
        self.rect = pygame.Rect(x,y,300,300)
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 50
        self.vel_y = 50
        self.targetRow = 0
        self.elapsed = 0
        self.updateRate = 250
        self.frame = 0
        self.direction = [0,0]
        self.shoot = 0   
        self.position = 0
        self.seek = False
        self.walk = False
        self.attack = False
        self.firing = False
        self.hp = 10
    def update(self, minwidth, maxwidth, deltaTime, player, aiRects):
        dt = deltaTime / 1000.0
        ddx = (player.rect.centerx - self.rect.centerx)**2
        ddy = (player.rect.centery - self.rect.centery)**2
        bounce = False
       #This section keeps tiger on screen	
        if self.direction[0] == 1 and self.direction[1] != 1:
            self.targetRow = 1
            futurerect = self.rect.move(self.vel_x*dt, 0)
            if futurerect.right >= maxwidth:
                self.direction[0] = 0
                self.direction[1] = 1
                bounce = True
            for tile in aiRects:
                if futurerect.colliderect(tile):
                    bounce = True
                    self.direction[0] = 0
                    self.direction[1] = 1
            if not bounce:
                self.rect = futurerect
        
        if self.direction[1] == 1 and self.direction[0] != 1:
            self.targetRow = 0
            futurerect = self.rect.move(-self.vel_x*dt, 0)
            if futurerect.left <= minwidth:
                self.direction[0] = 1
                self.direction[1] = 0
                bounce = True
            for tile in aiRects:
                if futurerect.colliderect(tile):
                    bounce = True
                    self.direction[0] = 1
                    self.direction[1] = 0
            if not bounce:
                self.rect = futurerect

        if self.rect.colliderect(player.rect):
            self.vel_x = 0
        else:
            self.vel_x = 50
        
        if math.sqrt(ddx + ddy) <= 350:
            self.seek = True
            self.walk = True
            self.attack = False
        else: 
            self.seek = False
            self.walk = True
            self.attack = False
        
        if math.sqrt(ddx + ddy) <= 300:
            self.attack = True
            self.walk = False
            self.firing = False
            
        if self.seek == True:
            if player.rect.centerx < self.rect.centerx:
                self.direction[0] = 0
                self.direction[1] = 1
            elif player.rect.centerx > self.rect.centerx:
                self.direction[1] = 0
                self.direction[0] = 1   
            
        
        self.elapsed += deltaTime
        if self.elapsed > self.updateRate:
            self.frame = (self.frame +1) % 4
            self.elapsed = 0
    
    def move(self):
        self.direction[0] = random.choice([0,1])
        self.direction[1] = not self.direction[0]
        #sets the monster either going left or right
	
    def vomit (self, screen):
        screen.blit(self.vomit_image, self.rect, pygame.Rect(0, self.targetRow*300,300,300))
    
    def draw(self, screen):
        if self.walk == True:
            screen.blit(self.image, self.rect, pygame.Rect(self.frame*300, self.targetRow*300,300,300))
        if self.attack == True:
            screen.blit(self.attack_image, self.rect, pygame.Rect(self.frame*300, self.targetRow*300,300,300))