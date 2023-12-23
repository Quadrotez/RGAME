import pygame, cd
from configparser import ConfigParser

import trydc

config = ConfigParser();
config.read('config.ini')
import cd


class Player:
    def __init__(self,
                 win):  # Специальный метод, который автоматически выполняется при создании каждого экземпляра класса. Принимает параметр self + *args
        self.win = win
        self.player_rect = pygame.Rect(cd.player_pos_x, cd.player_pos_y,
                                       int(config['PLAYER']['SIZE_X']), int(config['PLAYER']['SIZE_Y']))

    def blit(self):
        pygame.draw.rect(self.win, eval(config['PLAYER']['COLOR']),
                         [cd.player_pos_x, cd.player_pos_y,
                          int(config['PLAYER']['SIZE_X']), int(config['PLAYER']['SIZE_Y'])])


class Target:
    def __init__(self,
                 win):  # Специальный метод, который автоматически выполняется при создании каждого экземпляра класса. Принимает параметр self + *args
        self.win = win
        self.target_rect = pygame.Rect(cd.target_pos_x, cd.target_pos_y,
                                       int(config['TARGET']['SIZE_X']), int(config['TARGET']['SIZE_Y']))

    def blit(self):
        pygame.draw.rect(self.win, eval(config['TARGET']['COLOR']),
                         [cd.target_pos_x, cd.target_pos_y,
                          int(config['TARGET']['SIZE_X']), int(config['TARGET']['SIZE_Y'])])


class Scores:
    def __init__(self,
                 win):
        self.text_surface = pygame.font.Font(None, 36).render(f'Ваши очки: {str(cd.scores)} | Рекорд: {trydc.fsconfig["GENERAL"]["RECORD"]}', True, eval(config['COLORS']['TEXTCOLOR']), eval(config['COLORS']['BACKGROUND']))
        self.win = win
        self.text_rect = self.text_surface.get_rect()

    def blit(self):
        self.win.blit(self.text_surface, self.text_rect)
        self.text_surface = pygame.font.Font(None, 36).render(f'Ваши очки: {str(cd.scores)} | Рекорд: {trydc.fsconfig["GENERAL"]["RECORD"]}', True, eval(config['COLORS']['TEXTCOLOR']),
                                                              eval(config['COLORS']['BACKGROUND']))



class Blit():
    def __init__(self, win):
        self.win = win

        self.scores = Scores(self.win)
        self.player = Player(self.win)
        self.target = Target(self.win)


    def blit(self):
        self.player.blit()

        self.target.blit()

        self.scores.blit()

        pygame.display.update()

        pygame.display.flip()
