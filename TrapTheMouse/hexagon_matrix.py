"""
    This module contains the function to draw a matrix of hexagons.
"""
from hexagon import Hexagon

width, height = 900, 700


def draw_hexagon_matrix(surface, rows, cols):
    """
    Draws a matrix of hexagons.
    :param surface: surface of the pygame window
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: draws a matrix of hexagons
    """
    hexagon = Hexagon(25)
    for row in range(rows):
        for col in range(cols):
            x = col * hexagon.width + width * 0.45
            y = row * hexagon.height + height / 10
            if col % 2 == 1:
                y += hexagon.height / 2
            hexagon.draw(surface, x, y)
