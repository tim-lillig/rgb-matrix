import numpy as np

from spotify_app import main as sp
from view_matrix import main as vm
from resize_image import *
import pygame

GRID_WIDTH = 64
GRID_HEIGHT = 32
CELL_SIZE = 24

if __name__ == '__main__':
    # Initialize Pygame
    display_screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('Grid Renderer')

    # Get track info
    curr_track = sp.get_current_track()
    track_information = sp.get_track_info(curr_track)

    # Get resized image as pixel values
    resized_image = resize_image_and_get_pixel_values(track_information['album_image'], (30, 30))

    black_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH, 3))
    black_grid[1:31, 1:31] = resized_image

    vm.render_pixels(black_grid, display_screen)

