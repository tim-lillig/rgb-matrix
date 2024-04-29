import numpy as np

from apps.components import view_matrix_pygame as vm, spotify_functionality as sp
from apps.components.resize_image import *
import pygame

GRID_WIDTH = 64
GRID_HEIGHT = 32
CELL_SIZE = 16


def initialize_background():
    title_icon = [[[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                  [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]],
                  [[0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0]],
                  [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0]],
                  [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0]]]

    artist_icon = [[[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                   [[0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0]],
                   [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                   [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
                   [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]]

    # Place bg_matrix template
    bg = np.zeros((GRID_HEIGHT, GRID_WIDTH, 3))
    bg[1:31, 1:31] = np.ones((30, 30, 3), dtype=np.uint8) * 255
    bg[1:6, 32:36] = title_icon
    bg[7:12, 32:36] = artist_icon

    return bg


if __name__ == '__main__':
    # Initialize Pygame
    display_screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('Spotify App')

    # Initialize bg_matrix
    bg_matrix = initialize_background()

    # initialize spotify client
    spotify_client = sp.initialize_spotify()

    try:
        curr_track = sp.get_current_track(spotify_client)
        track_information = sp.get_track_info(curr_track, spotify_client)

        # get title and artist as pixel values
        #title = np.ones((5, 30, 3), dtype=np.uint8) * 255
        #artist = np.ones((5, 30, 3), dtype=np.uint8) * 255

        # Get resized image as pixel values
        album_cover = resize_image_and_get_pixel_values(track_information['album_image'], (30, 30))

        # Place attributes in bg_matrix
        #bg_matrix[1:6, 38:62] = title
        #bg_matrix[7:12, 38:62] = artist
        bg_matrix[1:31, 1:31] = album_cover

    except:
        print("Error getting track info")

    vm.render_pixels(bg_matrix, display_screen)
