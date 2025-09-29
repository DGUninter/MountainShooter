import pygame

# C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Ship1': 300,
    'Ship1Shot': 1,
    'Ship2': 300,
    'Ship2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Ship1': 1,
    'Ship1Shot': 25,
    'Ship2': 1,
    'Ship2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Ship1': 0,
    'Ship1Shot': 0,
    'Ship2': 0,
    'Ship2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Ship1': 20,
    'Ship2': 15,
    'Enemy1': 75,
    'Enemy2': 100
}

EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 6,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,

    'Ship1': 3,
    'Ship1Shot': 3,
    'Ship2': 3,
    'Ship2Shot': 3,

    'Enemy1': 2,
    'Enemy1Shot': 4,
    'Enemy2': 2,
    'Enemy2Shot': 3,
}

# M2
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COOPERATIVE',
               'SCORE',
               'EXIT')
# S
SHIP_KEY_UP = {'Ship1': pygame.K_UP,
               'Ship2': pygame.K_w}
SHIP_KEY_DOWN = {'Ship1': pygame.K_DOWN,
                 'Ship2': pygame.K_s}
SHIP_KEY_LEFT = {'Ship1': pygame.K_LEFT,
                 'Ship2': pygame.K_a}
SHIP_KEY_RIGHT = {'Ship1': pygame.K_RIGHT,
                  'Ship2': pygame.K_d}
SHIP_KEY_SHOT = {'Ship1': pygame.K_RCTRL,
                  'Ship2': pygame.K_LCTRL}

SPAWN_TIME = 4000
# M
MIN_WIDTH = 576
MIN_HEIGHT = 324
