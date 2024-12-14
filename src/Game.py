import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Gravity Tetris")   
        self.clock = pygame.time.Clock()
        
        # self.board = Board(20, 20)
        #self.current_piece = Tetriminoe.generate_piece
        #self.next_piece = Tetriminoe.generate_piece()
        self.gravity_direction = "DOWN"
        self.score = 0
        self.running = True
        
    def start(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()
            self.clock.tick(60) 
            
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)
    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    
    def update(self):
        pass
    
    
if __name__ == "__main__":
    game = Game()
    game.start()
    