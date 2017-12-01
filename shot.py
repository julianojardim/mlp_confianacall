import block
import config

class Shot(block.Block):
    def __init__(self, position, width, height, image, speed, target_pos, damage, effect):
        super(Shot, self).__init__(position, width, height, image)
        self._speed = speed
        self._direction = self.calculate_direction(target_pos)
        self._damage = damage
        self._effect = effect

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_damage(self):
        return self._damage

    def calculate_direction(self, target_pos):
        vector = target_pos[0] - self._position[0], target_pos[1] - self._position[1]
        vector = vector[0] / 4, vector[1] / 4
        return vector

    def move(self, tower):
        if self._position[0] > 1000 or self._position[0] < 0:
            self.destroy(tower)
        elif self._position[1] > 1000 or self._position[1] < 0:
            self.destroy(tower)
        else:
            new_position_X = self._position[0] + self._direction[0]
            new_position_Y = self._position[1] + self._direction[1]
            self.set_position((new_position_X, new_position_Y))

    def destroy(self, tower):
        tower.del_shot(self)