import pygame as py


PLAYER_COLOR = 0xE5C2C0
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800


class Player(object):
    def __init__(self, screen):
        self.screen = screen
        self.speed = 3
        self.alive = True
        self.player_rect = py.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, 10, 10)

    def draw(self):
        # draw player rect
        py.draw.rect(self.screen, PLAYER_COLOR, self.player_rect)

    def kill(self):
        self.alive = False
