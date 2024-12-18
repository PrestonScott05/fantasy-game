import pygame
import sys
import Map 
import Player

BACKGROUND_COLOR = 0x29222F
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("fantasy crawler")   
        self.clock = pygame.time.Clock()
        self.running = True
        
    def start(self):
        self.player = Player.Player(self.screen) #create player
        self.map = Map.Map(self.screen) #create map
        while self.running:
            self.process_events()
            self.player.move() 
        #draw game elements in layers -> things are drawn on top of each other in the order they are drawn
            self.screen.fill(BACKGROUND_COLOR) 
            self.map.draw()
            self.player.draw()
            pygame.display.flip()
            self.clock.tick(60) 
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)

        
        
    
    
if __name__ == "__main__":
    game = Game()
    game.start()
    