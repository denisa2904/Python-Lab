"""
    Main file for the game Trap the Mouse.
    This script draws the window and runs the game.
"""

import pygame

from game_board import GameBoard
from menu import Menu
from helpers.button import is_button_clicked

LIGHT_GREEN = (43, 175, 98)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 900, 700
MENU_WIDTH, MENU_HEIGHT = 700, 500


def main():
    pygame.init()
    board = GameBoard(11, 11)
    menu = Menu()

    menu_screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
    pygame.display.set_caption("Trap the Mouse")

    menu_active = True
    start_game = False
    running = True
    selector_active = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if not start_game:
                    if menu_active:
                        if is_button_clicked(x, y, menu.first_button):
                            selector_active = True
                            menu_active = False
                        elif is_button_clicked(x, y, menu.second_button):
                            start_game = True
                            menu_active = False
                    elif selector_active:
                        if is_button_clicked(x, y, menu.first_button):
                            start_game = True
                            selector_active = False
                        elif is_button_clicked(x, y, menu.second_button):
                            start_game = True
                            selector_active = False
                        elif is_button_clicked(x, y, menu.third_button):
                            start_game = True
                            selector_active = False

        if selector_active:
            menu_screen.fill(WHITE)
            menu.draw_ai_level_selector(menu_screen)
            pygame.display.flip()
            continue

        if menu_active:
            menu_screen.fill(WHITE)
            menu.draw_menu(menu_screen)
            pygame.display.flip()
            continue

        if start_game:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Trap the Mouse")
            screen.fill(LIGHT_GREEN)
            board.draw(screen)
            start_game = False
            continue

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
