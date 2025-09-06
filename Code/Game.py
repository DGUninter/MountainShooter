#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import MIN_HEIGHT, MIN_WIDTH
from Code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(MIN_WIDTH, MIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
