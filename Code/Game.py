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
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #        print('Quiting')
            #        pygame.quit()  # Close window
            #        quit()  # end pygame
