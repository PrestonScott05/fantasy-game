import pygame as py

PLAYER_COLOR = 0xE5C2C0
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

class Player(object):
    def __init__(self, screen):
        self.screen = screen
        self.speed = 3
        self.alive = True
        self.player_rect = py.Rect(SCREEN_WIDTH // 2, 200, 10, 10) 
        
        
    def draw(self):
        py.draw.rect(self.screen, PLAYER_COLOR, self.player_rect)
        
    def move(self):
        if self.alive:
            x_direction, y_direction = self.handle_move_inputs()
            self.player_rect.x += x_direction * self.speed
            self.player_rect.y += y_direction * self.speed
    
    
    def handle_move_inputs(self):
        keys = py.key.get_pressed()

    # handling for strafing        
        if keys[py.K_w] and keys[py.K_a]:
            return -1, -1
        elif keys[py.K_w] and keys[py.K_d]:
            return 1, -1
        elif keys[py.K_s] and keys[py.K_a]:
            return -1, 1
        elif keys[py.K_s] and keys[py.K_d]:
            return 1, 1
    # handling for cardinal directions
        elif keys[py.K_w]: 
            return 0, -1
        elif keys[py.K_s]:
            return 0, 1
        elif keys[py.K_a]:
            return -1, 0
        elif keys[py.K_d]:  
            return 1, 0  
    # no key pressed
        else:
            return 0, 0
            
    
    def kill(self):
        self.alive = False
         