#!/usr/bin/python3
from classes.gameobject import GameObject


class Spaceship(GameObject):

	def __init__(self, size):

		super(Spaceship, self).__init__("./resources/images/spaceship.png")
		pos = (
			size[0] / 2 - self.image_rect.width / 2,
			size[1] - self.image_rect.height
		)
		self.init_pos(pos)
