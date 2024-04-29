import pygame
import numpy as np
import os

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)  # Adjust the shade of gray as needed

# Define grid size and cell size
GRID_WIDTH = 64
GRID_HEIGHT = 32
CELL_SIZE = 24


def render_pixels(grid_values, screen):
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw the grid lines
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(screen, GRAY, (0, y * CELL_SIZE), (GRID_WIDTH * CELL_SIZE, y * CELL_SIZE), 1)
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(screen, GRAY, (x * CELL_SIZE, 0), (x * CELL_SIZE, GRID_HEIGHT * CELL_SIZE), 1)

        # Draw the pixels based on the input grid values
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grid_values[y][x] == 1:
                    pygame.draw.rect(screen, BLACK,
                                     (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


# Example usage
if __name__ == "__main__":
    # Initialize Pygame
    display_screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('Grid Renderer')

    # Create a sample grid with filled pixels
    sample_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))

    # Render the pixels
    render_pixels(sample_grid, display_screen)
