#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
from Code.Const import MIN_WIDTH, MIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (MIN_WIDTH, 0)))
                return list_bg

            case 'Ship1':
                return Player('Ship1', (10, MIN_HEIGHT / 2 - 30))
            case 'Ship2':
                return Player('Ship2', (10, MIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (MIN_WIDTH + 10, random.randint(30, MIN_HEIGHT - 30)))
            case 'Enemy2':
                return Enemy('Enemy2', (MIN_WIDTH + 10, random.randint(30, MIN_HEIGHT - 30)))
