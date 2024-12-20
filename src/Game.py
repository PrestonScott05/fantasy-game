import pygame
import sys
import Map
import Player

BACKGROUND_COLOR = 0x29222F
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

# TODO: FIX STICKY COLLIIONS
# TODO: BEGIN WORK ON ENEMIES
# TODO: ONLY RENDER WALLS TOUCHING AIR


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("fantasy crawler")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.player = Player.Player(self.screen)  # create player
        self.map = Map.Map(self.screen, self.player)  # create map
        drawables = [self.map, self.player]
        while self.running:
            self.process_events()
            # movement
            x_d, y_d = self.handle_move_inputs()
            self.map.move_map_around_player(x_direction=x_d, y_direction=y_d)
            # draw game elements in layers -> things are drawn on top of each other in the order they are drawn
            self.screen.fill(BACKGROUND_COLOR)
            for d in drawables:
                d.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit(0)

    def check_collisions(self, x_d, y_d):
        offset_x = -x_d * self.player.speed
        offset_y = -y_d * self.player.speed
        for wall in self.map.rect_grid:
            future_wall = wall.move(offset_x, offset_y)
            if self.player.player_rect.colliderect(future_wall):
                return True
        return False

    def handle_move_inputs(self):
        keys = pygame.key.get_pressed()
        # handling for strafing
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        # Vertical direction
        if keys[pygame.K_w]:
            dy = -1
        elif keys[pygame.K_s]:
            dy = 1
        # Horizontal direction
        if keys[pygame.K_a]:
            dx = -1
        elif keys[pygame.K_d]:
            dx = 1
        # Now check for collisions once
        if self.check_collisions(dx, dy):
            dx, dy = 0, 0
        return dx, dy
