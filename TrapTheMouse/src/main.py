"""
    Main file for the game Trap the Mouse.
    This script starts the game.
"""

import pygame

from objects.game import Game

LIGHT_GREEN = (43, 175, 98)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 900, 630
MENU_WIDTH, MENU_HEIGHT = 700, 500


def main():
    pygame.init()
    game = Game()
    game.run()

    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # menu_screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
    # pygame.display.set_caption("Trap the Mouse")
    #
    # menu_active = True
    # start_game = False
    # running = True
    # selector_active = False
    # play = False
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #         if pygame.mouse.get_pressed()[0]:
    #             x, y = pygame.mouse.get_pos()
    #             if not start_game:
    #                 if menu_active:
    #                     if is_button_clicked(x, y, menu.first_button):
    #                         selector_active = True
    #                         menu_active = False
    #                     elif is_button_clicked(x, y, menu.second_button):
    #                         start_game = True
    #                         menu_active = False
    #                 elif selector_active:
    #                     if is_button_clicked(x, y, menu.first_button):
    #                         start_game = True
    #                         selector_active = False
    #                     elif is_button_clicked(x, y, menu.second_button):
    #                         start_game = True
    #                         selector_active = False
    #                     elif is_button_clicked(x, y, menu.third_button):
    #                         start_game = True
    #                         selector_active = False
    #                 elif play:
    #                     if is_button_clicked(x, y, board.reset_button):
    #                         board = GameBoard(11, 11)
    #                         start_game = True
    #                         play = False
    #                     if is_button_clicked(x, y, board.back_button):
    #                         play = False
    #                         menu_active = True
    #                         pygame.quit()
    #                         pygame.init()
    #                         menu_screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
    #                         pygame.display.set_caption("Trap the Mouse")
    #                         menu.draw_menu(menu_screen)
    #                         pygame.display.flip()
    #                     else:
    #                         row, col = board.get_hexagon(x, y)
    #                         if not board.matrix[row][col].is_obstacle and not board.matrix[row][col].is_mouse:
    #                             board.matrix[row][col].set_obstacle()
    #
    #     if selector_active:
    #         menu.draw_ai_level_selector(menu_screen)
    #         pygame.display.flip()
    #         continue
    #
    #     if menu_active:
    #         menu.draw_menu(menu_screen)
    #         pygame.display.flip()
    #         continue
    #
    #     if start_game:
    #         screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #         pygame.display.set_caption("Trap the Mouse")
    #         screen.fill(LIGHT_GREEN)
    #         board.draw(screen)
    #         start_game = False
    #         play = True
    #         continue
    #
    #     if play:
    #         board.draw(screen)
    #         pygame.display.flip()
    #         continue
    #
    #     pygame.display.flip()
    #
    # pygame.quit()


if __name__ == "__main__":
    main()
