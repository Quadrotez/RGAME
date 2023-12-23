import random
import trydc

import objects

import pygame, sys, cd
pygame.init()

from configparser import ConfigParser
config = ConfigParser(); config.read('config.ini')

class Controls:
    def __init__(self):
        self.keys = pygame.key.get_pressed()
    def read_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                cd.running = False

        if (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]) and cd.player_pos_x > 0:
            cd.player_pos_x -= float(config['PLAYER']['SPEED'])

        elif (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]) and cd.player_pos_x < cd.screen_size_x - int(config['PLAYER']['SIZE_X']):
            cd.player_pos_x += float(config['PLAYER']['SPEED'])


        if (self.keys[pygame.K_UP] or self.keys[pygame.K_w]) and cd.player_pos_y > 0:
            cd.player_pos_y -= float(config['PLAYER']['SPEED'])

        elif (self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]) and cd.player_pos_y < cd.screen_size_y - int(config['PLAYER']['SIZE_Y']):
            cd.player_pos_y += float(config['PLAYER']['SPEED'])


        if objects.Player(cd.win).player_rect.colliderect(objects.Target(cd.win).target_rect):
            a, b = (random.randint(int(config['TARGET']['SIZE_X']), cd.screen_size_x - int(config['TARGET']['SIZE_X'])),
                    random.randint(int(config['TARGET']['SIZE_Y']), cd.screen_size_y - int(config['TARGET']['SIZE_Y'])))

            a = int(config['WIN']['HEIGHT']) if a <= 0 else a

            b = int(config['WIN']['WIDTH']) if b <= 0 else b

            # if a - int(config['TARGET']['SIZE_X'])


            cd.target_pos_x = a
            cd.target_pos_y = b

            cd.scores += 1

            if cd.scores > int(trydc.fsconfig['GENERAL']['RECORD']):
                trydc.fsconfig.set('GENERAL', 'RECORD', str(cd.scores))
                with open(trydc.fsconfig_path, 'w', encoding='UTF-8') as f:
                    trydc.fsconfig.write(f)