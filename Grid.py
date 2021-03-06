import random

import numpy as np

from Value import *
from graphics import *


# Classe per rappresentare la griglia
class Grid:
    def __init__(self, dim=10):
        self.dim = dim
        self.pixel_grid = list()
        self.colors = list()

        # Fill colors list of all the gamma of colors of a rainbow
        for i in range(6):
            for j in range(255):
                if i == 0:
                    self.colors.append(color_rgb(255, j, 0))
                elif i == 1:
                    self.colors.append(color_rgb(255 - j, 255, 0))
                elif i == 2:
                    self.colors.append(color_rgb(0, 255, j))
                elif i == 3:
                    self.colors.append(color_rgb(0, 255 - j, 255))
                elif i == 4:
                    self.colors.append(color_rgb(j, 0, 255))
                elif i == 5:
                    self.colors.append(color_rgb(255, 0, 255 - j))

    # Clean the grid
    def reset_grid(self):
        self.pixel_grid.clear()

    """
    Set the pixels of the grid in a random position and
    assign to each pixel a specific color of the gamma.
    """
    def shuffle(self):
        self.reset_grid()

        # It creates a linear space of dim dimension spaced from 0 to len of colors list
        linear_space = np.linspace(0, len(self.colors) - 1, num=self.dim)

        for i in range(self.dim):
            random_x = random.randint(0, self.dim)
            random_y = random.randint(0, self.dim)
            random_value = random.randint(0, self.dim - 1)
            self.pixel_grid.append(Value(random_x, random_y, random_value))

            color_from_linspace = int(linear_space[random_value])
            color = self.colors[color_from_linspace]

            self.pixel_grid[i].set_color(color)
