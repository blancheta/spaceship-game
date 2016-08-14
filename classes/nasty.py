#!/usr/bin/python3
from classes.gameobject import GameObject


class Nasty(GameObject):

	def __init__(self, pos):

		super(Nasty, self).__init__("./resources/images/invader.png")
		self.init_pos(pos)
