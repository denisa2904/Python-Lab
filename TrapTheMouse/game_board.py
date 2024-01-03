"""
    This module contains the GameBoard class.
"""
import random

from hexagon import Hexagon

WIDTH, HEIGHT = 900, 700


class GameBoard:
    """
        This class represents the game board.
    """

    def __init__(self, rows, cols):
        """
        Initializes the GameBoard class.
        :param rows: number of rows
        :param cols:  number of columns
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[Hexagon(25, i, j) for i in range(cols)] for j in range(rows)]
        self.matrix[5][5].set_mouse()
        self.random_obstacles()

    def random_obstacles(self):
        """
        Sets random obstacles on the game board.
        :return: sets random obstacles on the game board
        """
        n = random.randint(3, 7)
        for i in range(n):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if not self.matrix[row][col].is_mouse and not self.matrix[row][col].is_obstacle:
                self.matrix[row][col].set_obstacle()
            else:
                n += 1

    def draw(self, surface):
        """
        Draws the game board (matrix of hexagons).
        :param surface: surface of the pygame window
        :return: draws a matrix of hexagons
        """
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.matrix[row][col].width + WIDTH * 0.45
                y = row * self.matrix[row][col].height + HEIGHT / 10
                if col % 2 == 1:
                    y += self.matrix[row][col].height / 2
                self.matrix[row][col].draw(surface, x, y)
