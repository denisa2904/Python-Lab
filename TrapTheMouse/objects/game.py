"""
    This module contains the Game class.
"""
import pygame


from objects.game_board import GameBoard
from helpers.text import win
from objects.menu import Menu
from helpers.button import is_button_clicked

LIGHT_GREEN = (43, 175, 98)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 900, 630
MENU_WIDTH, MENU_HEIGHT = 700, 500
MOVES_ODD_ROW = [(0, 1), (0, -1), (-1, 0), (-1, 1), (1, 0), (1, 1)]
MOVES_EVEN_ROW = [(0, 1), (0, -1), (-1, 0), (-1, -1), (1, 0), (1, -1)]


class Game:
    """
        This class represents the game.
    """

    def __init__(self):
        """
            Initializes the Game class.
        """
        self.board = GameBoard(11, 11)
        self.menu = Menu()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.menu_screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
        pygame.display.set_caption("Trap the Mouse")

        self.menu_active = True
        self.start_game = False
        self.running = True
        self.selector_active = False
        self.play = False

        self.ai_level = 1
        self.is_human_opponent = False
        self.trapper_turn = True

        self.mouse_position = (5, 5)
        self.moves = MOVES_ODD_ROW

    def check_win_mouse(self):
        """
            Checks if the mouse won.
            :return: True if the mouse won, False otherwise
        """
        if self.mouse_position[0] == 0 or self.mouse_position[0] == self.board.rows - 1:
            win("Mouse", self.screen)
            return True
        if self.mouse_position[1] == 0 or self.mouse_position[1] == self.board.cols - 1:
            win("Mouse", self.screen)
            return True
        return False

    def check_win_trapper(self):
        """
            Checks if the trapper won.
            :return: True if the trapper won, False otherwise
        """
        for move in self.moves:
            row = self.mouse_position[0] + move[0]
            col = self.mouse_position[1] + move[1]
            if not self.board.matrix[row][col].is_obstacle:
                return False
        win("Trapper", self.screen)

        return True

    def find_coordinates(self, x, y):
        """
            Finds the coordinates of the hexagon.
            :param x: x coordinate of the mouse click
            :param y: y coordinate of the mouse click
            :return: the coordinates of the hexagon
        """
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if (self.board.matrix[row][col].is_inside(x, y) and not self.board.matrix[row][col].is_obstacle
                        and not self.board.matrix[row][col].is_mouse):
                    return row, col
        return -1, -1

    def trapper_move(self, x, y):
        """
            Moves for the one who wants to trap the mouse.
            :param x: x coordinate of the mouse click
            :param y: y coordinate of the mouse click
            :return: plays the game vs human
        """
        self.check_win_mouse()
        row, col = self.find_coordinates(x, y)
        if row == -1 and col == -1:
            return
        self.board.matrix[row][col].set_obstacle()
        self.board.matrix[row][col].is_obstacle = True
        self.trapper_turn = False
        self.board.trapper_turn = False
        self.board.draw(self.screen)
        self.check_win_trapper()

    def mouse_move(self, x, y):
        """
            Moves for the mouse.
            :param x: x coordinate of the mouse click
            :param y: y coordinate of the mouse click
            :return: plays the game vs human
        """
        self.check_win_trapper()
        pygame.display.flip()

        row, col = self.find_coordinates(x, y)
        if row == -1 and col == -1:
            return
        row_diff = row - self.mouse_position[0]
        col_diff = col - self.mouse_position[1]
        if (row_diff, col_diff) in self.moves:
            self.board.matrix[self.mouse_position[0]][self.mouse_position[1]].is_mouse = False
            self.board.matrix[row][col].set_mouse()
            self.board.matrix[row][col].is_mouse = True
            self.mouse_position = (row, col)
            self.trapper_turn = True
            self.board.trapper_turn = True

        self.check_win_mouse()
        self.board.draw(self.screen)
        if self.mouse_position[0] % 2 == 1:
            self.moves = MOVES_ODD_ROW
        else:
            self.moves = MOVES_EVEN_ROW

    def back_menu(self):
        """
            Goes back to the menu.
            :return: goes back to the menu
        """
        self.menu_active = True
        self.play = False
        self.start_game = False
        self.selector_active = False
        pygame.init()
        self.menu_screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
        pygame.display.set_caption("Trap the Mouse")
        self.menu.draw_menu(self.menu_screen)
        pygame.display.flip()

    def run(self):
        """
            Runs the game.
            :return: runs the game
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    if not self.start_game:
                        if self.menu_active:
                            if is_button_clicked(x, y, self.menu.first_button):
                                self.selector_active = True
                                self.menu_active = False
                            elif is_button_clicked(x, y, self.menu.second_button):
                                self.start_game = True
                                self.menu_active = False
                                self.is_human_opponent = True
                                pygame.time.wait(200)
                        elif self.selector_active:
                            if is_button_clicked(x, y, self.menu.first_button):
                                self.start_game = True
                                self.selector_active = False
                                self.ai_level = 1
                            elif is_button_clicked(x, y, self.menu.second_button):
                                self.start_game = True
                                self.selector_active = False
                                self.ai_level = 2
                            elif is_button_clicked(x, y, self.menu.third_button):
                                self.start_game = True
                                self.selector_active = False
                                self.ai_level = 3
                        elif self.play:
                            if is_button_clicked(x, y, self.board.back_button):
                                self.back_menu()
                            if is_button_clicked(x, y, self.board.reset_button):
                                self.board = GameBoard(11, 11)
                                self.start_game = True
                                self.play = False

                            if self.trapper_turn:
                                self.board.trapper_turn = True
                                self.trapper_move(x, y)
                            else:
                                self.board.trapper_turn = False
                                if self.is_human_opponent:
                                    self.mouse_move(x, y)
                                # else:
                                #     if self.ai_level == 1:
                                #         self.ai_easy_mouse_move(x, y)
                                #     elif self.ai_level == 2:
                                #         self.ai_medium_mouse_move(x, y)
                                #     elif self.ai_level == 3:
                                #         self.ai_hard_mouse_move(x, y)

            if self.selector_active:
                self.menu.draw_ai_level_selector(self.menu_screen)
                pygame.display.flip()
                continue

            if self.menu_active:
                self.menu.draw_menu(self.menu_screen)
                pygame.display.flip()
                continue

            if self.start_game:
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("Trap the Mouse")
                screen.fill(LIGHT_GREEN)
                self.play = True
                self.start_game = False
                self.board.draw(self.screen)
                pygame.display.flip()
                continue

            if self.play:
                self.board.draw(self.screen)
                pygame.display.flip()
                continue

            pygame.display.flip()

        pygame.quit()
