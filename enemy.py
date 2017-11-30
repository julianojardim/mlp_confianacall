from mlp import block


class Enemy(block.Block):
    def __init__(self, position, width, height, image, health, speed, earn_money, life_damage, first_dir, multiplier):
        super(Enemy, self).__init__(position, width, height, image)
        self._health = health * multiplier
        self._speed = speed
        self._start_speed = speed
        self._earn_money = earn_money * multiplier
        self._life_damage = life_damage
        self._up_flag = False
        self._down_flag = False
        self._right_flag = False
        self._left_flag = False
        self._set_start_flags(first_dir)

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

    def set_earn_money(self, earn_money):
        self._earn_money = earn_money

    def get_life_damage(self):
        return self._life_damage

    def set_life_damage(self, life_damage):
        self._life_damage = life_damage

