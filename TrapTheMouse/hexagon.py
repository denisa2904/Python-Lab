"""
    This module contains the Hexagon class.
"""
import math
import pygame

width, height = 900, 700
BORDER_COLOR_DARK_GREEN = (21, 87, 49)
FILL_COLOR_GREEN = (32, 131, 74)
BORDER_COLOR_DARK_BROWN = (135, 62, 35)
FILL_COLOR_BROWN = '#935139'
IMAGE = pygame.image.load("images/mouse1.png")
IMAGE_SIZE = (50, 50)
IMAGE = pygame.transform.scale(IMAGE, IMAGE_SIZE)


class Hexagon:
    """
        This class represents a hexagon.
    """

    def __init__(self, radius, row, col):
        """
        Initializes the Hexagon class.
        :param radius: the radius of the hexagon
        :param row: the row of the hexagon
        :param col: the column of the hexagon
        """
        self.radius = radius
        self.width = math.sqrt(3) * radius
        self.height = 2 * radius
        self.row = row
        self.col = col
        self.x = col * self.width + width * 0.45
        self.y = row * self.height + height / 10
        self.is_obstacle = False
        self.is_mouse = False

    def set_obstacle(self):
        """
        Sets the hexagon as an obstacle.
        :return: sets the hexagon as an obstacle
        """
        self.is_obstacle = True

    def set_mouse(self):
        """
        Sets the hexagon as the mouse.
        :return: sets the hexagon as the mouse
        """
        self.is_mouse = True

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
        if self.is_obstacle:
            pygame.draw.polygon(surface, FILL_COLOR_BROWN, points, 0)
            pygame.draw.polygon(surface, BORDER_COLOR_DARK_BROWN, points, 6)
        else:
            pygame.draw.polygon(surface, FILL_COLOR_GREEN, points, 0)
            pygame.draw.polygon(surface, BORDER_COLOR_DARK_GREEN, points, 6)

        if self.is_mouse:
            surface.blit(pygame.transform.scale(IMAGE, IMAGE_SIZE), (x - self.radius, y - self.radius))
