import pygame

from settings import *

colors = {
    0: BACKGROUND_COLOR,
    1: WALLS_COLOR,
    2: DOOR_COLOR
}


class PacManTile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.color = colors.get(tile_id, BACKGROUND_COLOR)

    def render(self, screen, x, y):
        pygame.draw.rect(screen, self.color,
                         (x, y, CELL_SIZE, CELL_SIZE))