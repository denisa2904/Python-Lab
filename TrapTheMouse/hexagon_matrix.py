from hexagon import Hexagon

width, height = 900, 700


def draw_hexagon_matrix(surface, rows, cols):
    hexagon = Hexagon(25)
    for row in range(rows):
        for col in range(cols):
            x = col * hexagon.width + width * 0.45
            y = row * hexagon.height + height / 10
            if col % 2 == 1:
                y += hexagon.height / 2
            hexagon.draw(surface, x, y)
