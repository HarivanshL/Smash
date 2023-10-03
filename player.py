import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player, pos, width, height):
        super().__init__()
        self.player = player
        self.image = pygame.Surface((width, height))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
        self.movable = True
        self.gravity = 0.2
        self.jump_speed = -4
        self.vector = pygame.Vector2(0,0)
        self.speed = 2
        self.jumpCount = 0
        self.jumpable = True
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rect)

    def get_input(self):
        if self.movable:
            if self.player == 1:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.jump()
                if keys[pygame.K_a]:
                    self.vector.x = -1
                elif keys[pygame.K_d]:
                    self.vector.x = 1
                else:
                    self.vector.x =0
                    #self.jump()
            if self.player == 2:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    self.jump()
                if keys[pygame.K_LEFT]:
                    self.vector.x = -1
                elif keys[pygame.K_RIGHT]:
                    self.vector.x = 1
                else:
                    self.vector.x = 0
                    #self.jump()

    def horizontal_movement_collision(self, tiles):

        #self.rect.x += self.vector.x * self.speed
        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.rect.colliderect(self):
                    if self.vector.x < 0:
                         self.rect.left = sprite.rect.right
                    elif self.vector.x > 0:
                        self.rect.right = sprite.rect.left

    def vertical_movement_collision(self, tiles):

        #self.apply_gravity()
        #self.rect.y += self.vector.y * self.speed
        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.vector.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.vector.y = 0

    
    def jump(self):
        if self.jumpCount < 2 and self.jumpable:
            self.vector.y = self.jump_speed
            self.jumpCount += 1       
            


        self.vector.y = self.jump_speed
    def apply_gravity(self):
        self.vector.y += self.gravity
        self.rect.y += self.vector.y
    def move(self):
        self.rect.x += self.vector.x * self.speed
        self.rect.y += self.vector.y * self.speed

    def update(self, sprites):
        self.get_input()
        self.apply_gravity()
        self.vertical_movement_collision(sprites)
        self.horizontal_movement_collision(sprites)
        self.move()
