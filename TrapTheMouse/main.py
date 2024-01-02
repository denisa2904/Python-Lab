"""
    Main file for the game Trap the Mouse.
    This script draws the window and runs the game.
    Usage: python main.py
"""
import pygame
from game_board import GameBoard


LIGHT_GREEN = (43, 175, 98)

width, height = 900, 700


def main():
    pygame.init()
    board = GameBoard(11, 11)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Trap the Mouse")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if pygame.mouse.get_pressed()[0]:
            #     x, y = pygame.mouse.get_pos()
            #     board.element_clicked(x, y)

        screen.fill(LIGHT_GREEN)
        board.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
