import pygame
from lists import*
# Classe que define a unidade básica do cenário, tudo que aparece na cena deriva dela


class Block(object):
    def __init__(self, position, width, height, image):
        self._position = position  # top left
        self._width = width
        self._height = height
        self._image = pygame.image.load(image)
        self._image_string = image

    def collide(self, block_two):
        block_two_pos = block_two.getPosition()
        block_two_width, block_two_height = block_two.getDims()
        position1 = (first(block_two_pos) + 1, second(block_two_pos) + 1)
        position2 = (first(block_two_pos) + block_two_pos - 1, second(block_two_pos) + 1)
        position3 = (first(block_two_pos) + block_two_width - 1, second(block_two_pos) + block_two_height - 1)
        position4 = (first(block_two_pos) + 1, second(block_two_pos) + block_two_height - 1)
        if self.is_inside(position1) or self.is_inside(position2) or self.is_inside(position3) or self.is_inside(position4):
            return True
        else:
            return False

    def block_center(self):
        return int(first(self._position) + .5 * self._width), int(second(self._position) + .5 * self._height)

    def set_image(self, image):
        self._image = pygame.image.load(image)

    def get_image(self):
        return self._image

    def get_image_string(self):
        return self._image_string

    def get_position(self):
        return self._position

    def set_position(self, pos):
        self._position = pos
        self.block_center()

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        self.block_center()

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
        self.block_center()

    def get_dimens(self):
        return self.get_width(), self.get_height()

    def draw(self, surface):
        surface.blit(self._image, self._position)

    def is_inside(self, position):
        if self._position[0] <= position[0] < self._position[0] + self._width and self._position[1] <= position[1] < \
                        self._position[1] + self._height:
            return True
        else:
            return False
