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
    mouse_down = False
    mouse_dragged_cells = set()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
                # Get the mouse position
                mouse_x, mouse_y = event.pos
                # Calculate the grid position based on the mouse position
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                # Check if the grid coordinates are within bounds
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    # Toggle the cell color if not already toggled during this drag operation
                    if (grid_x, grid_y) not in mouse_dragged_cells:
                        grid_values[grid_y][grid_x] = 1.0 - grid_values[grid_y][grid_x]
                        mouse_dragged_cells.add((grid_x, grid_y))
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                mouse_dragged_cells.clear()  # Clear the set after releasing the mouse button
            elif event.type == pygame.MOUSEMOTION and mouse_down:
                # Get the mouse position
                mouse_x, mouse_y = event.pos
                # Calculate the grid position based on the mouse position
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                # Check if the grid coordinates are within bounds
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    # Toggle the cell color if not already toggled during this drag operation
                    if (grid_x, grid_y) not in mouse_dragged_cells:
                        grid_values[grid_y][grid_x] = 1.0 - grid_values[grid_y][grid_x]
                        mouse_dragged_cells.add((grid_x, grid_y))

        screen.fill(WHITE)

        # Draw the grid lines
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(screen, GRAY, (0, y * CELL_SIZE), (GRID_WIDTH * CELL_SIZE, y * CELL_SIZE), 1)
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(screen, GRAY, (x * CELL_SIZE, 0), (x * CELL_SIZE, GRID_HEIGHT * CELL_SIZE), 1)

        # Draw the pixels based on the input grid values
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color_value = int(grid_values[y][x] * 255)
                color = (color_value, color_value, color_value)
                pygame.draw.rect(screen, color, (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1))

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

    # Folder containing the files
    folder_path = "output_files"

    # Get a list of files in the folder
    files = os.listdir(folder_path)

    # Find the maximum number in the existing file names
    max_num = 0
    for file_name in files:
        if file_name.startswith("grid_") and file_name.endswith(".txt"):
            try:
                num = int(file_name.split("_")[1].split(".")[0])
                max_num = max(max_num, num)
            except ValueError:
                pass

    # Increment the maximum number by 1 to get the new grid name
    new_grid_name = f"grid_{max_num + 1:03d}.txt"
    final_path = "output_files/" + new_grid_name

    with open(final_path, "w") as f:
        f.write(repr(grid_values.tolist()))


# Example usage
if __name__ == "__main__":
    # Initialize Pygame
    display_screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('Pixel Renderer')

    # Generate a grid with all cells initially white
    white_grid = np.ones((GRID_HEIGHT, GRID_WIDTH))
    black_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
    render_pixels(white_grid, display_screen)
