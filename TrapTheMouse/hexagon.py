import math
import pygame


class Hexagon:
    def __init__(self, radius):
        self.radius = radius
        self.border_color_dark_green = (21, 87, 49)
        self.fill_color_green = (32, 131, 74)
        self.width = math.sqrt(3) * radius
        self.height = 2 * radius

    def draw(self, surface, x, y):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            hx = x + self.radius * math.cos(angle)
            hy = y + self.radius * math.sin(angle)
            points.append((hx, hy))
        pygame.draw.polygon(surface, self.fill_color_green, points, 0)
        pygame.draw.polygon(surface, self.border_color_dark_green, points, 6)
