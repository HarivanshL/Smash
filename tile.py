import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__() 
        self.image = pygame.Surface((width, height))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
    
    def adjust(self, zoom):
        #self.image = pygame.transform.scale(self.image, (self.image.get_width() * zoom, self.image.get_height() * zoom))
        self.rect.w = self.rect.w * zoom
        self.rect.h = self.rect.h * zoom
        self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))

    def shift(self, xamount, yamount):
        self.rect.x += xamount
        self.rect.y += yamount