#!/usr/bin/python3
import pygame
from screens.game import Game
from screens.menu import GameMenu
from screens.settings import GameSettings

pygame.init()

# set_mode(resolution=(width, height), flags=0, depth=0)
# flags : collection of qdditional options
# depth : number of bits use for colors
screen = pygame.display.set_mode((640, 480), 0, 32)
bg_color = (0, 0, 0)

# Game Menu
pygame.display.set_caption('Game Menu')
menu_items = ('Start', 'Settings', 'Quit')

# Views initialization
gm = GameMenu(screen, menu_items)
gs = GameSettings(screen)
g = None

menu_selected = True
mainloop = True
while mainloop:

	screen.fill(bg_color)
	if menu_selected or g.escape_selected:
		gm.run()
		if g is not None:
			g.escape_selected = False
		gs.escape_selected = False

	if gm.start_selected:
		pygame.display.set_caption('Game')
		g = Game(screen)
		g.run()
		gm.start_selected = False
		gm.quit_select = False

	if gm.settings_selected:
		gs.run()
		gm.settings_selected = False

	if gm.quit_select is True:
		mainloop = False

	pygame.display.flip()
