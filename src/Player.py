import pygame as py

PLAYER_COLOR = 0xE5C2C0
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

class Player(object):
    def __init__(self, screen):
        self.screen = screen
        self.player_rect = py.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10) 
         
        py.draw.rect(self.screen, PLAYER_COLOR, self.player_rect)
    
    def move_player(self, player):
        # TODO: Implement movement logic here
        pass
    
    
    def handle_move_inputs(self):
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            self.direction = (0, 1)
        elif keys[py.K_s]:
            self.direction = (1, 0)
        elif keys[py.K_a]:
            self.direction = (-1, 0)
        elif keys[py.K_d]:  
            self.direction = (0, -1)
            
        return self.direction
         