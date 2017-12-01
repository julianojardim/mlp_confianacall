import pygame
import config
import board
import enemie

class Game:
    def __init__(self):
        self._exit_game = False
        self._noCashTimer = 0
        self._FPS = 0
        self._display = 0
        self._clock = 0
        self._background_image = pygame.image.load(config.Config.GAME_WINDOW)
        self._enemie_image = pygame.image.load(config.Config.IMAGE_GRASS)

    def set_exit_game(self):
        self._exit_game = True

    def get_exit_game(self):
        return self._exit_game

    def set_display(self, display):
        self._display = display

    def get_display(self):
        return self._display

    def set_clock(self, clock):
        self._clock = clock

    def get_clock(self):
        return self._clock

    def turn_on_fps(self):
        self._FPS = True

    def turn_off_fps(self):
        self._FPS = False

    def is_fps_on(self):
        return self._FPS

    def start(self):
        pygame.init()
        self._display = pygame.display.set_mode((config.Config.MENU_WIDTH, config.Config.MENU_HEIGHT+200))
        pygame.display.set_caption("Py.defense")
        self._clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # 1 second is 1000 milliseconds

    def start_wave(self):
        inimigo = enemie.Enemie((100, 60),40,40,config.Config.IMAGE_GRASS, 100, 1, 100, 20, 1, 1)
        inimigo.set_display(self._display)
        inimigo.wave(inimigo.get_flag_list())

    def display_game(self):
        self._display.blit(self._background_image, (0, 0))


    def update(self):
        pygame.display.update()

    def quit(self):
        pygame.quit()

    def paint_all_stuff(self, display, clock):
        if self.is_fps_on():
           self.paint_fps(display, clock.get_fps())

    def paint_fps(self, display, fps):
        font = pygame.font.SysFont(None, 25)
        text = font.render("FPS = %.2f" % fps, True, (0,0,0))
        display.blit(text, (0, 0))

novo_jogo = Game()
novo_jogo.start()