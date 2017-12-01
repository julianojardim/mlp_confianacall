import block
import board
import game
import config
import pygame
from lists import*


class Enemie(block.Block):
    def __init__(self, position, width, height, image, health, speed, earn_money, life_damage, first_dir, multiplier):
        super(Enemie, self).__init__(position, width, height, image)
        self._health = health * multiplier
        self._speed = speed
        self._start_speed = speed
        self._earn_money = earn_money * multiplier
        self._life_damage = life_damage
        self._display = 0
        self._up_flag = False
        self._down_flag = False
        self._right_flag = False
        self._left_flag = False
        #self._set_start_flags(first_dir)
        self._start_position = (100, 60)
        self._stop = False
        self._flag_list = [1,1,
                           2,2,2,2,2,2,2,2,2,2,2,2,
                           1,1,1,1,1,1,
                           3,3,3,
                           0,0,0,
                           3,3,3,3,3,3,3,3,3,
                           1,1,1,
                           2,2,2,2,2,2,2,
                           1,1,1,
                           3,3,3,3,3,3,3,
                           1,1,
                           2,2,2,2,2,2,2,2,2,
                           0,0,0,
                           2,2,
                           1,1,1,1,
                           2,2]
        self._clock = pygame.time.Clock()
        self._fps = 20
    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def refresh_speed(self):
        self._speed = self._start_speed

    def get_earn_money(self):
        return self._earn_money

    def get_flag_list(self):
        return self._flag_list

    def set_earn_money(self, earn_money):
        self._earn_money = earn_money

    def set_display(self, display):
        self._display = display


    def get_life_damage(self):
        return self._life_damage

    def set_life_damage(self, life_damage):
        self._life_damage = life_damage

#    def set_start_flags(self, first_dir):
#        if first_dir == 0:
#            self._up_flag = True
#        elif first_dir == 1:
#           self._down_flag = True
#        elif first_dir == 2:
#            self._left_flag = True
#        elif first_dir == 3:
#            self._right_flag = True

    def spawn(self):
        self.set_position(self._start_position)

    def move(self, deslocamento):
        (x, y) = self.get_position()
        if self._up_flag and (deslocamento != 0):
            self.set_position((x, y-(1*self._speed)))
            self.move(deslocamento-1)
        if self._down_flag and (deslocamento != 0):
            self.set_position((x, y+(1*self._speed)))
            self.move(deslocamento - 1)
        if self._left_flag and (deslocamento != 0):
            self.set_position((x-(1*self._speed), y))
            self.move(deslocamento - 1)
        if self._right_flag and (deslocamento != 0):
            self.set_position((x+(1*self._speed), y))
            self.move(deslocamento - 1)

    def set_flags(self, list):
        if not is_empty(list):
            if first(list) == 0:
                self._up_flag = True
                self._down_flag = False
                self._right_flag = False
                self._left_flag = False

            elif first(list) == 1:
                self._up_flag = False
                self._down_flag = True
                self._right_flag = False
                self._left_flag = False

            elif first(list) == 2:
                self._up_flag = False
                self._down_flag = False
                self._right_flag = True
                self._left_flag = False

            elif first(list) == 3:
                self._up_flag = False
                self._down_flag = False
                self._right_flag = False
                self._left_flag = True

    def print_enemie(self, display):
        display.blit(self.get_image(), self.get_position())

    def wave(self, list):
        self.set_flags(list)
        if not is_empty(list):
            if self._up_flag:
                self.move(40)
            elif self._down_flag:
                self.move(40)
            elif self._right_flag:
                self.move(40)
            elif self._left_flag:
                self.move(40)
            self.wave(rest(list))
