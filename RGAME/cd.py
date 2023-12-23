import random, trydc
from configparser import ConfigParser
config = ConfigParser(); config.read('config.ini')

# INIT

#WIN
win = None
screen_size_x = int(config['WIN']['WIDTH'])
screen_size_y = int(config['WIN']['HEIGHT'])
if int(config['WIN']['WIDTH']) == 0 and int(config['WIN']['HEIGHT']) == 0:
    screen_size_x = int(trydc.fsconfig['GENERAL']['SCREEN_SIZE_X'])
    screen_size_y = int(trydc.fsconfig['GENERAL']['SCREEN_SIZE_Y'])

# OBJECTS
# PLAYER
player_pos_x = int(config['PLAYER']['POS_X'])
player_pos_y = int(config['PLAYER']['POS_Y'])

# TARGET
target_pos_x = random.randint(0, screen_size_x - int(config['TARGET']['SIZE_X']))
target_pos_y = random.randint(0, screen_size_y - int(config['TARGET']['SIZE_Y']))

# SCORES
scores = int(config['GENERAL']['SCORES'])

# GENERAL
running = eval(config['GENERAL']['RUNNING'])

