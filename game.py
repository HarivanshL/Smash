import pygame
from settings import *
from level import Level
class game():
    def __init__(self):     
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Brawl_Theme.mp3")
        self.tile_size = tile_size
        self.background_colour = (234, 212, 252)
        screen_width, screen_height =  len(level[0]) *tile_size,  len(level) * tile_size,
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.level = Level(self.screen, level)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.level.setup_level1()
        pygame.display.set_caption('Scroller')
        
        self.screen.fill(self.background_colour)

        self. playingMusic = False
        self.running = True
    def playMusic(self):
        if not self.playingMusic:
            pygame.mixer.music.play(-1)
            self.playingMusic = True
# game loop
    def game_loop(self):
                
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((234, 212, 252))
            self.level.run()
            self.playMusic()
            pygame.display.flip()
            self.clock.tick(60)
g = game()

g.game_loop()
pygame.display.quit()