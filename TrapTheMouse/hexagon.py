
"""
    This module contains the Hexagon class.
"""
import math
import pygame


class Hexagon:
    """
        This class represents a hexagon.
    """
    def __init__(self, radius):
        """
        Initializes the Hexagon class.
        :param radius: the radius of the hexagon
        """
        self.radius = radius
        self.border_color_dark_green = (21, 87, 49)
        self.fill_color_green = (32, 131, 74)
        self.width = math.sqrt(3) * radius
        self.height = 2 * radius

    def draw(self, surface, x, y):
        """
        Draws a hexagon.
        :param surface: surface of the pygame window
        :param x: x coordinate of the hexagon
        :param y: y coordinate of the hexagon
        :return: draws a hexagon
        """
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            hx = x + self.radius * math.cos(angle)
            hy = y + self.radius * math.sin(angle)
            points.append((hx, hy))
        pygame.draw.polygon(surface, self.fill_color_green, points, 0)
        pygame.draw.polygon(surface, self.border_color_dark_green, points, 6)
