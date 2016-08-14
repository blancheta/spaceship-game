#!/usr/bin/python3
from classes.gameobject import GameObject


class Life(GameObject):

	def __init__(self, pos):

		super(Life, self).__init__("./resources/images/spaceship_mini.png")
		self.init_pos(pos)
