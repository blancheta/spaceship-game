#!/usr/bin/python3
import os
import sys
import pygame
from game import Game
from gamemenu import GameMenu
from gamesettings import GameSettings

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

# Game Menu
pygame.display.set_caption('Game Menu')
menu_items = ('Start','Settings','Quit')
gm = GameMenu(screen,menu_items)

# Settings
gs = GameSettings(screen)
bg_color = (0,0,0)

mainloop = True
while mainloop:
	screen.fill(bg_color)
	g = None
	if (gm.quit_select == False or gm.start_selected == False) or g.escape_selected == True or gs.escape_selected:
		gm.run()
		if g is not None:
			g.escape_selected = False
		gs.escape_selected = False

	if gm.start_selected:
		g = Game(screen)
		g.run()
		gm.start_selected = False
		gm.quit_select = False

	if gm.settings_selected:
		gs.run()
		gm.settings_selected = False
		
	if gm.quit_select == True:
		mainloop = False

	pygame.display.flip()