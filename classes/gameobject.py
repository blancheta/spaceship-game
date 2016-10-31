#!/usr/bin/python3
import pygame


class GameObject:

	def __init__(self, image):

		# Init image
		self.image = pygame.image.load(image)
		self.sprite = self.image.get_rect()

	def init_pos(self, pos):

		# Init position
		self.sprite.x, self.sprite.y = pos
