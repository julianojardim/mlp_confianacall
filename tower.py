# coding=utf-8
import config
import block
import pygame
import abc
import shot


# Classe Tower estende de Rectangle:
# Essa classe define as Torres do jogo, tanto as que serão postas no mapa,
# como as que ficam na aba de compras.
class Tower(block.Block, metaclass=abc.ABCMeta):
    _mouseCircleSurface = pygame.Surface(config.Config.MOUSE_CIRCLE_SURFACE)

    def __init__(self, position, width, height, image, range, damage, fire_rate, price):
        super(Tower, self).__init__(position, width, height, image)
        self._range = range
        self._rangeLevel = 1
        self._upgradeRangePrice = 40
        self._damage = damage
        self._damageLevel = 1
        self._upgradeDamagePrice = 50
        self._fireRate = fire_rate
        self._effectLevel = 1
        self._upgradeEffectPrice = 40
        self._reloadTime = 1 / fire_rate
        self._price = price
        self._shotList = []

    def get_first_class(self):
        return "Tower"

    @abc.abstractmethod
    def get_class(self):
        return

    @abc.abstractmethod
    def new_copy(self):
        return

    def get_range(self):
        return self._range

    def set_range(self, range):
        self._range = range

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage

    def get_fire_rate(self):
        return self._fireRate

    def set_fire_rate(self, fireRate):
        self._fireRate = fireRate

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_shot_list(self):
        return self._shotList

    def get_upgrade_damage_price(self):
        return self._upgradeDamagePrice

    def upgrade_damage(self):
        self._damageLevel += 1
        self._damage = config.Config.TOWER_DAMAGE * 1.3 ** (self._damageLevel - 1)
        self._upgradeDamagePrice = self._upgradeDamagePrice + 10 * self._damageLevel ** 1.5

    def get_upgrade_range_price(self):
        return self._upgradeRangePrice

    def upgrade_range(self):
        self._rangeLevel += 1
        self._range += 10
        self._upgradeRangePrice = self._upgradeRangePrice + 10 * self._rangeLevel ** 1.5

    def get_upgrade_effect_price(self):
        return self._upgradeEffectPrice

    def upgrade_effect(self):
        self._effectLevel += 1
        self._upgradeEffectPrice = self._upgradeEffectPrice + 10 * self._effectLevel ** 1.5

    def double_price(self):
        self._price *= 2

    def dec_reload_time(self):
        self._reloadTime -= 1.0

    def reset_reload_time(self):
        self._reloadTime = 1.0 / self._fireRate
        #print self._reloadTime

    def shot_enemies(self, enemies):
        if self._reloadTime <= 0:
            for enemieAux in enemies:
                if self.is_inside_range(enemieAux.getPosition()):
                    self.shot(enemieAux)
                    self.reset_reload_time()
                    break

    @abc.abstractmethod
    def shot(self, enemie):
        pass

    def move_shots(self, gameDisplay, enemieList, towerDefense):
        for shot_aux in self._shotList:
            shot_aux.move(self)
            for enemieAux in enemieList:
                if enemieAux.collide(shot_aux):
                    if shot_aux.getEffect() != "NULL":
                        enemieAux.setEffect(shot_aux.getEffect())
                    enemieAux.hit(shot_aux.get_damage(), towerDefense)
                    shot_aux.destroy(self)
                    break
        self.paint_shots(gameDisplay)

    def del_shot(self, shot):
        try:
            self._shotList.remove(shot) #Dar uma olhada aqui
        except:
            pass

    def paint_shots(self, gameDisplay):
        for shotAux in self._shotList:
            shotAux.paint(gameDisplay)

    def is_inside_range(self, position):
        center = self.block_center()
        if center[0] - self._range <= position[0] < center[0] + self._range:
            if center[1] - self._range <= position[1] < center[1] + self._range:
                return True
        return False

    def paint_range(self, gameDisplay, color):
        self._mouseCircleSurface.fill(config.Config.CK)
        self._mouseCircleSurface.set_colorkey(config.Config.CK)
        pygame.draw.circle(self._mouseCircleSurface, color, self.block_center(), self._range, self._range)
        self._mouseCircleSurface.set_alpha(150)
        gameDisplay.blit(self._mouseCircleSurface, (0, 0))

    def paint_atributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render("Damage:%d" % self._damage, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 177))
        text = font.render("Range:%d" % self._range, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 197))
        text = font.render("Fire Rate:%.2f" % self._fireRate, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 217))


class ClassicTower(Tower):
    def __init__(self, position):
        super(ClassicTower, self).__init__(position,
                                           config.Config.TOWER_WIDTH,
                                           config.Config.TOWER_HEIGHT,
                                           config.Config.TOWER_IMAGE_small,
                                           config.Config.TOWER_RANGE,
                                           config.Config.TOWER_DAMAGE,
                                           config.Config.TOWER_FIRERATE,
                                           config.Config.TOWER_PRICE)

    def get_class(self):
        return "ClassicTower"

    def new_copy(self):
        return ClassicTower(self._position)

    def shot(self, enemie):
        self._shotList.append(shot.Shot(self.get_position(), 8, 8, "imagens/shot.png", 0.5, enemie.getPosition(), self.get_damage(), "NULL"))


class ClassicTowerBuyer(Tower):
    def __init__(self, position):
        super(ClassicTowerBuyer, self).__init__(position,
                                                config.Config.TOWER_WIDTH * 2,
                                                config.Config.TOWER_HEIGHT * 2,
                                                #config.Config.TOWER_IMAGE_big,
                                                config.Config.TOWER_RANGE,
                                                config.Config.TOWER_DAMAGE,
                                                config.Config.TOWER_FIRERATE,
                                                config.Config.TOWER_PRICE)

    def get_class(self):
        return "ClassicTowerBuyer"

    def new_copy(self):
        return ClassicTowerBuyer(self._position)

    def shot(self, enemie):
        pass