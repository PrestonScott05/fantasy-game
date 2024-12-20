import pygame
import sys

# Configuration
GRID_COLS = 40     # Number of columns (bigger grid)
GRID_ROWS = 40 # Number of rows (bigger grid)
INITIAL_CELL_SIZE = 32
MIN_CELL_SIZE = 8
MAX_CELL_SIZE = 128

# Define colors for visualization
COLOR_BACKGROUND = (50, 50, 50)
COLOR_GRID = (100, 100, 100)
COLOR_HIGHLIGHT = (255, 255, 0)

# Assign colors for different tile types
# Key = tile type (int), Value = RGB tuple
TILE_COLORS = {
    0: (200, 200, 200),  # Default/empty
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (0, 0, 255)
}


def main():
    pygame.init()
    # Fixed window size
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pygame Level Editor with Zoom")

    clock = pygame.time.Clock()

    # Create a 2D array for the level data
    level_data = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

    current_tile_type = 1
    mouse_down = False
    cell_size = INITIAL_CELL_SIZE

    running = True
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // cell_size
        row = mouse_y // cell_size

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    current_tile_type = 1
                elif event.key == pygame.K_2:
                    current_tile_type = 2
                elif event.key == pygame.K_3:
                    current_tile_type = 3
                elif event.key == pygame.K_0:
                    current_tile_type = 0
                elif event.key == pygame.K_s:
                    # Print the current level data
                    print("Current level data:")
                    for row_data in level_data:
                        print(row_data)
                elif event.key == pygame.K_z:
                    # Zoom in
                    cell_size = min(cell_size + 8, MAX_CELL_SIZE)
                elif event.key == pygame.K_x:
                    # Zoom out
                    cell_size = max(cell_size - 8, MIN_CELL_SIZE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_down = True
                    # Paint immediately on click
                    if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
                        level_data[row][col] = current_tile_type

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False

        # If mouse is down, keep painting where the mouse is
        if mouse_down:
            if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
                level_data[row][col] = current_tile_type

        # Drawing
        screen.fill(COLOR_BACKGROUND)

        # Determine how many cells fit on the screen with current cell_size
        # We only draw what's visible in the current window
        visible_cols = WINDOW_WIDTH // cell_size + 1
        visible_rows = WINDOW_HEIGHT // cell_size + 1

        for r in range(min(visible_rows, GRID_ROWS)):
            for c in range(min(visible_cols, GRID_COLS)):
                tile_type = level_data[r][c]
                tile_color = TILE_COLORS[tile_type]
                rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, tile_color, rect)
                pygame.draw.rect(screen, COLOR_GRID, rect, 1)

        # Highlight the cell under the mouse if it's in range
        if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
            highlight_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, COLOR_HIGHLIGHT, highlight_rect, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

    # After quitting, print the final level data
    print("Final level data:")
    for row_data in level_data:
        print(row_data)


if __name__ == "__main__":
    main()
