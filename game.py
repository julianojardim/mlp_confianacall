import pygame
import config
import board


class Game:
    def __init__(self):
        self._exit_game = False
        self._noCashTimer = 0
        self._FPS = 0
        self._display = 0
        self._clock = 0

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