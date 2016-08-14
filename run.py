#!/usr/bin/python3
import pygame
from screens.game import Game
from screens.menu import GameMenu
from screens.settings import GameSettings

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

# Game Menu
pygame.display.set_caption('Game Menu')
menu_items = ('Start', 'Settings', 'Quit')
gm = GameMenu(screen, menu_items)

# Settings
gs = GameSettings(screen)
bg_color = (0, 0, 0)

mainloop = True
while mainloop:
	pass
