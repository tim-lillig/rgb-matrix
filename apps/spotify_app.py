import numpy as np

from apps.components import view_matrix_pygame as vm, spotify_functionality as sp
from apps.components.resize_image import *
import pygame

GRID_WIDTH = 64
GRID_HEIGHT = 32
CELL_SIZE = 24

if __name__ == '__main__':
    # Initialize Pygame
    display_screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('Spotify App')

    # initialize spotify client
    spotify_client = sp.initialize_spotify()

    try:
        curr_track = sp.get_current_track(spotify_client)
        track_information = sp.get_track_info(curr_track, spotify_client)

        # Get resized image as pixel values
        resized_image = resize_image_and_get_pixel_values(track_information['album_image'], (30, 30))
    except:
        print("Error getting track info")
        resized_image = np.ones((30, 30, 3), dtype=np.uint8) * 255

    # Generate a grid with all cells initially black
    black_grid = np.zeros((GRID_HEIGHT, GRID_WIDTH, 3))
    # Place album image on background
    black_grid[1:31, 1:31] = resized_image

    vm.render_pixels(black_grid, display_screen)
