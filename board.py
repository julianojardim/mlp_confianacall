import pygame
import config
from lists import*
import block


class Board:
    def __init__(self):
        self._board = [[0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3]]
        self._init_board = self._board
        self._board_centers = []
        self._board_width = len(self._board)
        self._board_height = len(first(self._board))
        self.line = range(1, 16)
        self.calc_centers_line()
        self._image_grass = pygame.image.load(config.Config.IMAGE_GRASS)
        self._image_path = pygame.image.load(config.Config.IMAGE_PATH)
        self._image_start = pygame.image.load(config.Config.IMAGE_START)
        self._image_finish = pygame.image.load(config.Config.IMAGE_FINISH)

    def calc_centers_line(self):
        list_aux = list(self.line)
        self._board_centers = list(map(lambda x: x*40, list_aux))

    def draw_board_line(self, display, board, centers, line):
        if not is_empty(board):
            if first(board) == 0:
                display.blit(self._image_grass, (int(first(centers)), line*40))
            elif first(board) == 1:
                display.blit(self._image_path, (int(first(centers)), line*40))
            elif first(board) == 2:
                display.blit(self._image_start, (int(first(centers)), line*40))
            elif first(board) == 3:
                display.blit(self._image_finish, (int(first(centers)), line*40))

            self.draw_board_line(display, rest(board), rest(centers), line)

    def draw_board(self, display, init_line):

        if not is_empty(self._board):
            self.draw_board_line(display, (first(self._board)), self._board_centers, init_line)
            init_line += 1
            self._board = rest(self._board)
            self.draw_board(display, init_line)

        self._board = self._init_board
#board1 = Board()
#print(board1._board_centers)