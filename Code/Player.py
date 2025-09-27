#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.Const import ENTITY_SPEED, MIN_HEIGHT, MIN_WIDTH, SHIP_KEY_UP, SHIP_KEY_DOWN, SHIP_KEY_LEFT, SHIP_KEY_RIGHT
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)

    #def update(self, ):
        #pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[SHIP_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[SHIP_KEY_DOWN[self.name]] and self.rect.bottom < MIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[SHIP_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[SHIP_KEY_RIGHT[self.name]] and self.rect.right < MIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass
