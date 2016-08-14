#!/usr/bin/python3
import sys
import pygame


class GameSettings:

	def __init__(self, screen):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.size = self.scr_width, self.scr_height

		# Background Game
		self.bg = pygame.image.load("resources/images/settings.jpg")
		self.bg_rect = self.bg.get_rect()
		self.escape_selected = False

	def run(self):

		mainloop = True
		while mainloop:

			# Redraw the background
			self.screen.fill((0, 0, 0))
			self.screen.blit(self.bg, self.bg_rect)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			keys = pygame.key.get_pressed()

			if keys[pygame.K_ESCAPE]:
				mainloop = False
				self.escape_selected = True

			pygame.display.flip()
